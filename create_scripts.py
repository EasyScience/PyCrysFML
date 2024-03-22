import os
import re
import sys
import json
import tomllib
import argparse

global ARGS
global CONFIG

def _project_dir():
    return os.path.dirname(__file__)

def _project_path():
    return os.path.abspath(_project_dir())

def _config_path(name: str):
    path = os.path.join(_project_dir(), name)
    path = os.path.abspath(path)
    return path

def _scripts_path():
    dir = CONFIG['dir']['scripts']
    path = os.path.abspath(dir)
    return path

def _main_script_path():
    name = 'main_script.sh'
    path = os.path.join(_scripts_path(), name)
    return path

def _echo_msg(msg: str):
    return f'echo "- {msg}"'

def _echo_progress_msg(current: int, total: int, msg: str):
    progress = _compiling_progress(current, total)
    msg = f"[{progress:>3}%] {msg}"
    return f'echo "  {msg}"'

def _echo_header(msg: str):
    msg = f':: {msg} ::'
    sep = ':' * len(msg)
    lines = []
    lines.append(f'echo ""')
    lines.append(f'echo "{sep}"')
    lines.append(f'echo "{msg}"')
    lines.append(f'echo "{sep}"')
    return lines

def _platform():
    if sys.platform.startswith('darwin'):
        return 'macos'
    elif sys.platform.startswith('lin'):
        return 'ubuntu'
    elif sys.platform.startswith('win'):
        return 'windows'
    else:
        print(f'- Unsupported platform: {sys.platform}')
        return None

def _fix_file_permissions(path: str):
    os.chmod(path, 0o777)

def _write_lines_to_file(lines: list, name: str):
    path = os.path.join(_scripts_path(), name)
    with open(path, 'w') as file:
        for line in lines:
            if _shell() == 'bash':
                line = line.replace('\\', '/')
            file.write(line + '\n')
    _fix_file_permissions(path)

def _total_src_file_count(modules: str):
    count = 0
    for module in CONFIG[modules]:
        if 'main-file' in module:
            count += 1
        if 'components-dir' in module and 'components-files' in module:
            for component_file in module['components-files']:
                count += 1
    return count

def _shell():
    shell = 'bash'  # default
    if ARGS.shell:
        shell = ARGS.shell
    return shell

def _compiler_name():
    compiler = 'gfortran'  # default
    if ARGS.compiler:
        compiler = ARGS.compiler
    return compiler

def _compiler_options():
    compiler = _compiler_name()
    mode = _compiling_mode()
    options = ''
    for build in CONFIG['build-objs']:
        if _platform() in build['platforms'] and compiler in build['compilers']:
            options = ' '.join(build['modes'][mode])
            break
    return options

def _obj_ext():
    compiler = _compiler_name()
    ext = ''
    for build in CONFIG['build-objs']:
        if _platform() in build['platforms'] and compiler in build['compilers']:
            ext = build['obj-ext']
            break
    return ext

def _compiler_build_shared_template():
    compiler = _compiler_name()
    template = ''
    for build in CONFIG['build-objs']:
        if _platform() in build['platforms'] and compiler in build['compilers']:
            template = build['build-shared']
            break
    return template

def _compiling_mode():
    mode = 'debug'  # default
    if ARGS.mode:
        mode = ARGS.mode
    return mode

def _compiling_progress(current: int, total: int):
    progress = round(current / total * 100)
    return progress

def _compile_objs_script_lines(modules: str, src_path: str, include_path: str=None):
    src_ext = CONFIG['build']['src-ext'][modules]
    modules = f'{modules}-modules'
    template_cmd = CONFIG['template']['build-obj']
    if include_path is None:
        template_cmd = template_cmd.replace(' -I {INCLUDE}', '')
    else:
        template_cmd = template_cmd.replace('{INCLUDE}', include_path)
    compiler = _compiler_name()
    options = _compiler_options()
    total = _total_src_file_count(modules)
    current = 0
    lines = []
    for module in CONFIG[modules]:
        if 'main-file' in module:
            current += 1
            name = f'{module["main-file"]}.{src_ext}'
            msg = _echo_progress_msg(current, total, f"{name}")
            lines.append(msg)
            path = os.path.join(src_path, name)
            cmd = template_cmd.replace('{COMPILER}', compiler).replace('{OPTIONS}', options).replace('{PATH}', path)
            lines.append(cmd)
        if 'components-dir' in module and 'components-files' in module:
            components_dir = module['components-dir']
            for component_file in module['components-files']:
                current += 1
                name = f'{component_file}.{src_ext}'
                path = os.path.join(components_dir, name)
                msg = _echo_progress_msg(current, total, f"{name}")
                lines.append(msg)
                path = os.path.join(src_path, path)
                cmd = template_cmd.replace('{COMPILER}', compiler).replace('{OPTIONS}', options).replace('{PATH}', path)
                lines.append(cmd)
    return lines

def _compile_shared_objs_or_dynamic_libs_script_lines(modules: str):
    obj_ext = _obj_ext()
    cfml_lib_name = CONFIG['cfml']['static-lib']['name']
    cfml_dist_dir = CONFIG['cfml']['dir']['dist']
    cfml_dist_path = os.path.join(_project_path(), cfml_dist_dir)
    cfml_lib_dist_dir = CONFIG['cfml']['dir']['dist-lib']
    cfml_lib_dist_path = os.path.join(cfml_dist_path, cfml_lib_dist_dir)
    python_lib = CONFIG['build']['python-lib'][_platform()]
    compiler = _compiler_name()
    template_cmd = _compiler_build_shared_template()
    shared_lib_ext = CONFIG['build']['shared-lib-ext'][_platform()]
    total = _total_src_file_count(modules)
    current = 0
    lines = []
    for module in CONFIG[modules]:
        if 'main-file' in module:
            current += 1
            name = f'{module["main-file"]}'
            msg = _echo_progress_msg(current, total, f'{name}.{obj_ext}')
            lines.append(msg)
            cmd = template_cmd
            cmd = cmd.replace('{COMPILER}', compiler)
            cmd = cmd.replace('{PATH}', name)
            cmd = cmd.replace('{EXT}', shared_lib_ext)
            cmd = cmd.replace('{CFML_LIB_PATH}', cfml_lib_dist_path)
            cmd = cmd.replace('{CFML_LIB_NAME}', cfml_lib_name)
            cmd = cmd.replace('{PYTHON_LIB}', python_lib)
            lines.append(cmd)
    return lines

def parsed_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--compiler", help="fortran compiler (gfortran, nagfor, ifx, ifort)")
    parser.add_argument("--mode", help="build mode (debug, release)")
    parser.add_argument("--shell", help="build mode (bash, powershell)")
    return parser.parse_args()

def loaded_config(name: str):
    path = _config_path(name)
    with open(path, 'rb') as f:
        return tomllib.load(f)

def clear_main_script():
    path = _main_script_path()
    with open(path, 'w') as file:
        pass

def append_to_main_script(obj: str | list):
    path = _main_script_path()
    if isinstance(obj, str):
        lines = [obj]
    if isinstance(obj, list):
        lines = obj
    with open(path, 'a') as file:
        for line in lines:
            if _shell() == 'bash':
                line = line.replace('\\', '/')
            file.write(line + '\n')
    _fix_file_permissions(path)

def show_info():
    platform = _platform()
    mode = _compiling_mode()
    compiler = _compiler_name()
    options = _compiler_options()
    lines = []
    msg = _echo_msg(f"Platform '{platform}'")
    lines.append(msg)
    msg = _echo_msg(f"Compiling mode '{mode}'")
    lines.append(msg)
    msg = _echo_msg(f"Fortran compiler '{compiler}'")
    lines.append(msg)
    #msg = _echo_msg(f"Compiler options '{options}'")
    #lines.append(msg)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def create_cfml_repo_dir():
    repo_dir = CONFIG['cfml']['dir']['repo']
    repo_path = os.path.join(_project_path(), repo_dir)
    lines = []
    msg = _echo_msg(f"Deleting build dir '{repo_dir}'")
    lines.append(msg)
    cmd = f'rm -rf {repo_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Creating build dir '{repo_dir}'")
    lines.append(msg)
    cmd = f'mkdir -p {repo_path}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def download_cfml_repo():
    project_name = CONFIG['cfml']['name']
    url = CONFIG['cfml']['git']['url']
    branch = CONFIG['cfml']['git']['branch']
    out_dir = CONFIG['cfml']['dir']['repo']
    out_path = os.path.abspath(out_dir)
    lines = []
    msg = _echo_msg(f"Downloading {project_name} branch '{branch}' to '{out_dir}' from '{url}'")
    lines.append(msg)
    template_cmd = CONFIG['template']['clone-repo']
    cmd = template_cmd.replace('{BRANCH}', branch).replace('{URL}', url).replace('{OUT_PATH}', out_path)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def create_cfml_build_dir():
    build_dir = CONFIG['cfml']['dir']['build']
    build_path = os.path.join(_project_path(), build_dir)
    lines = []
    msg = _echo_msg(f"Deleting build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'rm -rf {build_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Creating build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'mkdir -p {build_path}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def compile_cfml_objs():
    project_name = CONFIG['cfml']['name']
    repo_dir = CONFIG['cfml']['dir']['repo']
    src_dir = CONFIG['cfml']['dir']['repo-src']
    src_path = os.path.join(_project_path(), repo_dir, src_dir)
    build_dir = CONFIG['cfml']['dir']['build']
    build_path = os.path.join(_project_path(), build_dir)
    lines = []
    msg = _echo_msg(f"Entering build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {build_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Building fortran objects for {project_name}:")
    lines.append(msg)
    compile_lines = _compile_objs_script_lines('cfml', src_path)
    lines.extend(compile_lines)
    msg = _echo_msg(f"Exiting build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {_project_path()}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def create_cfml_static_lib():
    lib_ext = CONFIG['build']['static-lib-ext'][_platform()]
    static_lib_prefix = CONFIG['build']['static-lib-prefix'][_platform()]
    lib_name = CONFIG['cfml']['static-lib']['name']
    lib_name = f'{static_lib_prefix}{lib_name}'
    build_dir = CONFIG['cfml']['dir']['build']
    build_path = os.path.join(_project_path(), build_dir)
    lines = []
    msg = _echo_msg(f"Entering build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {build_path}'
    lines.append(cmd)

    lines.append(f'echo "11111"')
    lines.append(f'ls -l {build_path}')

    msg = _echo_msg(f"Creating fortran static library '{lib_name}.{lib_ext}'")
    lines.append(msg)
    template_cmd = CONFIG['template']['build-static'][_platform()]
    cmd = template_cmd.replace('{LIB}', lib_name)
    lines.append(cmd)

    lines.append(f'echo "22222"')
    lines.append(f'ls -l {build_path}')


    msg = _echo_msg(f"Exiting build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {_project_path()}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def create_cfml_dist_dir():
    dist_dir = CONFIG['cfml']['dir']['dist']
    dist_path = os.path.join(_project_path(), dist_dir)
    lib_dist_dir = CONFIG['cfml']['dir']['dist-lib']
    include_dist_dir = CONFIG['cfml']['dir']['dist-include']
    lib_dist_path = os.path.join(dist_path, lib_dist_dir)
    include_dist_path = os.path.join(dist_path, include_dist_dir)
    lines = []
    msg = _echo_msg(f"Deleting dist dir '{dist_dir}'")
    lines.append(msg)
    cmd = f'rm -rf {dist_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Creating dist dir '{dist_dir}'")
    lines.append(msg)
    cmd = f'mkdir -p {dist_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Creating dist dir '{dist_dir}/{lib_dist_dir}'")
    lines.append(msg)
    cmd = f'mkdir -p {lib_dist_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Creating dist dir '{dist_dir}/{include_dist_dir}'")
    lines.append(msg)
    cmd = f'mkdir -p {include_dist_path}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def copy_compiled_to_cfml_dist():
    lib_ext = CONFIG['build']['static-lib-ext'][_platform()]
    static_lib_prefix = CONFIG['build']['static-lib-prefix'][_platform()]
    lib_name = CONFIG['cfml']['static-lib']['name']
    lib_name = f'{static_lib_prefix}{lib_name}'
    build_dir = CONFIG['cfml']['dir']['build']
    build_path = os.path.join(_project_path(), build_dir)
    dist_dir = CONFIG['cfml']['dir']['dist']
    dist_path = os.path.join(_project_path(), dist_dir)
    lib_dist_dir = CONFIG['cfml']['dir']['dist-lib']
    include_dist_dir = CONFIG['cfml']['dir']['dist-include']
    lib_dist_path = os.path.join(dist_path, lib_dist_dir)
    include_dist_path = os.path.join(dist_path, include_dist_dir)
    lines = []
    msg = _echo_msg(f"Copying compiled lib '{lib_name}.{lib_ext}' to dist dir '{dist_dir}/{lib_dist_dir}'")
    lines.append(msg)
    from_path = os.path.join(build_path, f'{lib_name}.{lib_ext}')
    cmd = f'cp {from_path} {lib_dist_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Copying compiled modules to dist dir '{dist_dir}/{include_dist_dir}'")
    lines.append(msg)
    from_path = os.path.join(build_path, '*.*mod')
    cmd = f'cp {from_path} {include_dist_path}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def create_pycfml_repo_dir():
    repo_dir = CONFIG['pycfml']['dir']['repo']
    repo_path = os.path.join(_project_path(), repo_dir)
    lines = []
    msg = _echo_msg(f"Deleting build dir '{repo_dir}'")
    lines.append(msg)
    cmd = f'rm -rf {repo_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Creating build dir '{repo_dir}'")
    lines.append(msg)
    cmd = f'mkdir -p {repo_path}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def download_pycfml_repo():
    project_name = CONFIG['pycfml']['name']
    url = CONFIG['pycfml']['git']['url']
    branch = CONFIG['pycfml']['git']['branch']
    out_dir = CONFIG['pycfml']['dir']['repo']
    out_path = os.path.abspath(out_dir)
    lines = []
    msg = _echo_msg(f"Downloading {project_name} branch '{branch}' to '{out_dir}' from '{url}'")
    lines.append(msg)
    template_cmd = CONFIG['template']['clone-repo']
    cmd = template_cmd.replace('{BRANCH}', branch).replace('{URL}', url).replace('{OUT_PATH}', out_path)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def add_powder_mod_to_pycfml_repo():
    cfml_project_name = CONFIG['cfml']['name']
    cfml_repo_dir = CONFIG['cfml']['dir']['repo']
    cfml_repo_path = os.path.join(_project_path(), cfml_repo_dir)
    pycfml_project_name = CONFIG['pycfml']['name']
    pycfml_repo_dir = CONFIG['pycfml']['dir']['repo']
    pycfml_src_dir = CONFIG['pycfml']['dir']['repo-src']
    pycfml_src_path = os.path.join(_project_path(), pycfml_repo_dir, pycfml_src_dir)
    src_ext = CONFIG['build']['src-ext']['pycfml']
    lines = []
    from_relpath = os.path.join('Testing', 'Powder', 'Test_2', 'fortran', 'src', f'powder_mod.{src_ext}')
    from_abspath = os.path.join(cfml_repo_path, from_relpath)
    msg = _echo_msg(f"Copying '{from_relpath}' to '{pycfml_repo_dir}/{pycfml_src_dir}'")
    lines.append(msg)
    cmd = f'cp {from_abspath} {pycfml_src_path}'
    lines.append(cmd)
    from_relpath = os.path.join('Testing', 'Powder', 'Test_3', f'powder_mod_2.{src_ext}')
    from_abspath = os.path.join(cfml_repo_path, from_relpath)
    msg = _echo_msg(f"Copying '{from_relpath}' to '{pycfml_repo_dir}/{pycfml_src_dir}'")
    lines.append(msg)
    cmd = f'cp {from_abspath} {pycfml_src_path}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def create_pycfml_build_dir():
    build_dir = CONFIG['pycfml']['dir']['build']
    build_path = os.path.join(_project_path(), build_dir)
    lines = []
    msg = _echo_msg(f"Deleting build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'rm -rf {build_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Creating build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'mkdir -p {build_path}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def compile_pycfml_objs():
    project_name = CONFIG['pycfml']['name']
    repo_dir = CONFIG['pycfml']['dir']['repo']
    src_dir = CONFIG['pycfml']['dir']['repo-src']
    src_path = os.path.join(_project_path(), repo_dir, src_dir)
    build_dir = CONFIG['pycfml']['dir']['build']
    build_path = os.path.join(_project_path(), build_dir)
    dist_dir = CONFIG['cfml']['dir']['dist']
    include_dist_dir = CONFIG['cfml']['dir']['dist-include']
    include_dist_path = os.path.join(_project_path(), dist_dir, include_dist_dir)
    lines = []
    msg = _echo_msg(f"Entering build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {build_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Building fortran objects for {project_name}:")
    lines.append(msg)
    compile_lines = _compile_objs_script_lines('pycfml', src_path, include_dist_path)
    lines.extend(compile_lines)
    msg = _echo_msg(f"Exiting build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {_project_path()}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def create_pycfml_shared_objs_or_dynamic_libs():
    project_name = CONFIG['pycfml']['name']
    build_dir = CONFIG['pycfml']['dir']['build']
    build_path = os.path.join(_project_path(), build_dir)
    lines = []
    msg = _echo_msg(f"Entering build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {build_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Building fortran shared objs or dynamic libs for {project_name}:")
    lines.append(msg)
    compile_lines = _compile_shared_objs_or_dynamic_libs_script_lines('pycfml-modules')
    lines.extend(compile_lines)
    msg = _echo_msg(f"Exiting build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {_project_path()}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def create_pycfml_dist_dir():
    dist_dir = CONFIG['pycfml']['dir']['dist']
    dist_abspath = os.path.join(_project_path(), dist_dir)
    package_dir = CONFIG['pycfml']['dir']['dist-package']
    package_relpath = os.path.join(dist_dir, package_dir)
    package_abspath = os.path.join(dist_abspath, package_dir)
    lines = []
    msg = _echo_msg(f"Deleting dist dir '{dist_dir}'")
    lines.append(msg)
    cmd = f'rm -rf {dist_abspath}'
    lines.append(cmd)
    msg = _echo_msg(f"Creating dist dir '{package_relpath}'")
    lines.append(msg)
    cmd = f'mkdir -p {package_abspath}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def copy_compiled_to_pycfml_dist():
    shared_lib_ext = CONFIG['build']['shared-lib-ext'][_platform()]
    project_name = CONFIG['pycfml']['name']
    build_dir = CONFIG['pycfml']['dir']['build']
    build_path = os.path.join(_project_path(), build_dir)
    dist_dir = CONFIG['pycfml']['dir']['dist']
    package_dir = CONFIG['pycfml']['dir']['dist-package']
    package_relpath = os.path.join(dist_dir, package_dir)
    package_abspath = os.path.join(_project_path(), dist_dir, package_dir)
    lines = []
    msg = _echo_msg(f"Copying compiled {project_name} shared objects or dynamic libs to '{package_relpath}'")
    lines.append(msg)
    from_path = os.path.join(build_path, f'*.{shared_lib_ext}')
    cmd = f'cp {from_path} {package_abspath}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def add_init_file_to_pycfml_dist():
    project_name = CONFIG['pycfml']['name']
    repo_dir = CONFIG['pycfml']['dir']['repo']
    repo_path = os.path.join(_project_path(), repo_dir)
    dist_dir = CONFIG['pycfml']['dir']['dist']
    package_dir = CONFIG['pycfml']['dir']['dist-package']
    package_relpath = os.path.join(dist_dir, package_dir)
    package_abspath = os.path.join(_project_path(), package_relpath)
    lines = []
    msg = _echo_msg(f"Copying {project_name} '__init__.py' to dist dir '{package_relpath}'")
    lines.append(msg)
    from_path = os.path.join(repo_path, 'pycrysfml08', '__init__.py')
    cmd = f'cp {from_path} {package_abspath}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def add_cfml_databases_to_pycfml_dist():
    cfml_repo_dir = CONFIG['cfml']['dir']['repo']
    cfml_src_dir = CONFIG['cfml']['dir']['repo-src']
    cfml_src_relpath = os.path.join(cfml_repo_dir, cfml_src_dir)
    pycfml_dist_dir = CONFIG['pycfml']['dir']['dist']
    pycfml_package_dir = CONFIG['pycfml']['dir']['dist-package']
    pycfml_package_relpath = os.path.join(pycfml_dist_dir, pycfml_package_dir)
    database_name = 'magnetic_data.txt'
    databases_dir = 'Databases'
    cfml_databases_relpath = os.path.join(cfml_src_relpath, databases_dir, database_name)
    cfml_databases_abspath = os.path.join(_project_path(), cfml_databases_relpath)
    pycfml_databases_relpath = os.path.join(pycfml_package_relpath, databases_dir)
    pycfml_databases_abspath = os.path.join(_project_path(), pycfml_databases_relpath)
    lines = []
    msg = _echo_msg(f"Creating dir '{pycfml_databases_relpath}'")
    lines.append(msg)
    cmd = f'mkdir -p {pycfml_databases_abspath}'
    lines.append(cmd)
    msg = _echo_msg(f"Copying '{cfml_databases_relpath}' database to dist dir '{pycfml_databases_relpath}'")
    lines.append(msg)
    cmd = f'cp {cfml_databases_abspath} {pycfml_databases_abspath}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def create_pycfml_python_wheel():
    project_name = CONFIG['pycfml']['name']
    wheel_dir = CONFIG['pycfml']['dir']['wheel']
    wheel_path = os.path.join(_project_path(), wheel_dir)
    lines = []
    msg = _echo_msg(f"Creating '{project_name}' python wheel in '{wheel_dir}'")
    lines.append(msg)
    template_cmd = CONFIG['template']['build-wheel']
    cmd = template_cmd.replace('{PATH}', wheel_path)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def install_pycfml_from_wheel():
    project_name = CONFIG['pycfml']['name']
    package_name = CONFIG['pycfml']['dir']['dist-package']
    wheel_dir = CONFIG['pycfml']['dir']['wheel']
    wheel_path = os.path.join(_project_path(), wheel_dir)
    lines = []
    msg = _echo_msg(f"Installing '{project_name}' python wheel from '{wheel_dir}'")
    lines.append(msg)
    template_cmd = CONFIG['template']['install-wheel']
    cmd = template_cmd.replace('{PACKAGE}', package_name).replace('{PATH}', wheel_path)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def run_pycfml_unit_tests():
    relpath = os.path.join('tests', 'unit_tests')
    abspath = os.path.join(_project_path(), relpath)
    lines = []
    msg = _echo_msg(f"Running unit tests from '{relpath}'")
    lines.append(msg)
    template_cmd = CONFIG['template']['run-tests']
    cmd = template_cmd.replace('{PATH}', abspath)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def run_powder_mod_tests():
    relpath = os.path.join('tests', 'powder_mod_tests')
    abspath = os.path.join(_project_path(), relpath)
    lines = []
    msg = _echo_msg(f"Running powder_mod tests from '{relpath}'")
    lines.append(msg)
    template_cmd = CONFIG['template']['run-tests']
    cmd = template_cmd.replace('{PATH}', abspath)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def run_powder_mod_main():
    relpath = os.path.join('tests', 'powder_mod_tests', 'test_powder_mod.py')
    abspath = os.path.join(_project_path(), relpath)
    lines = []
    msg = _echo_msg(f"Running powder_mod main from '{relpath}'")
    lines.append(msg)
    template_cmd = CONFIG['template']['run-python']
    cmd = template_cmd.replace('{PATH}', abspath)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

if __name__ == '__main__':
    ARGS = parsed_args()
    CONFIG = loaded_config('scripts_config.toml')
    cfml_project_name = CONFIG['cfml']['name']
    pycfml_project_name = CONFIG['pycfml']['name']

    clear_main_script()

    headers = _echo_header(f"Info")
    append_to_main_script(headers)
    show_info()

    headers = _echo_header(f"Creating {cfml_project_name} static library")
    append_to_main_script(headers)
    create_cfml_repo_dir()
    download_cfml_repo()
    create_cfml_build_dir()
    compile_cfml_objs()
    create_cfml_static_lib()
    create_cfml_dist_dir()
    copy_compiled_to_cfml_dist()

    headers = _echo_header(f"Creating {pycfml_project_name} shared objects or dynamic libraries")
    append_to_main_script(headers)
    create_pycfml_repo_dir()
    download_pycfml_repo()
    add_powder_mod_to_pycfml_repo()
    create_pycfml_build_dir()
    compile_pycfml_objs()
    create_pycfml_shared_objs_or_dynamic_libs()
    create_pycfml_dist_dir()
    copy_compiled_to_pycfml_dist()

    headers = _echo_header(f"Creating {pycfml_project_name} python package wheel")
    append_to_main_script(headers)
    add_init_file_to_pycfml_dist()
    add_cfml_databases_to_pycfml_dist()
    create_pycfml_python_wheel()

    headers = _echo_header(f"Installing {pycfml_project_name} from python wheel")
    append_to_main_script(headers)
    install_pycfml_from_wheel()

    headers = _echo_header(f"Running {pycfml_project_name} tests")
    append_to_main_script(headers)
    run_pycfml_unit_tests()
    run_powder_mod_tests()
    run_powder_mod_main()
