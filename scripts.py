import os
import sys
import site
import tomllib
import argparse
import sysconfig
import platform
from pygit2 import Repository

global ARGS
global CONFIG


def _github_actions():
    if 'GITHUB_ACTIONS' in os.environ:
        return True
    return False

def _github_branch():
    return Repository('.').head.shorthand

def _project_dir():
    return os.path.dirname(__file__)

def _project_path():
    return os.path.abspath(_project_dir())

def _config_path(name: str):
    path = os.path.join(_project_dir(), name)
    path = os.path.abspath(path)
    return path

def _scripts_path():
    dir = CONFIG['project']['dir']['scripts']
    path = os.path.abspath(dir)
    return path

def _main_script_path():
    name = 'main_script.sh'
    path = os.path.join(_scripts_path(), name)
    return path

def _echo_msg(msg: str):
    return f'echo ":::::: {msg}"'

def _echo_progress_msg(current: int, total: int, msg: str):
    progress = _compiling_progress(current, total)
    msg = f"[{progress:>3}%] {msg}"
    return f'echo "{msg}"'

def _echo_header(msg: str):
    msg = f':::::: {msg} ::::::'
    sep = ':' * len(msg)
    lines = []
    lines.append(f'echo ""')
    lines.append(f'echo "{sep}"')
    lines.append(f'echo "{msg}"')
    lines.append(f'echo "{sep}"')
    return lines

def _processor():
    processor = platform.processor()
    processor = processor.split()[0]  # get the 1st word from string, such as 'Intel64 Family 6 Model 154 Stepping 3, GenuineIntel'
    return processor

def _platform():
    platform = 'macos'  # default
    if ARGS.platform:
        platform = ARGS.platform.lower()
    return platform

def _platform_tag():
    tag = sysconfig.get_platform()
    tag = tag.replace('-', '_')
    tag = tag.replace('.', '_')
    return tag

def _python_version_full():  # full version, e.g., '3.11.6'
    return platform.python_version()

def _python_version_short():  # short version, e.g., '311'
    return sysconfig.get_config_var('py_version_nodot')

def _python_tag():  # tag, e.g., 'py311'
    return f'py{_python_version_short()}'

def _python_site_packages():
    site_packages = site.getsitepackages()
    site_packages = site_packages[0]  # get the first location from the list
    return site_packages

def _python_lib():
    if _platform() == 'macos':
        python_lib = '`python3-config --ldflags --embed`'
    elif _platform() == 'linux':
        python_lib = ''
    elif _platform() == 'windows':
        lib_file = f'python{_python_version_short()}.lib'
        python_lib = os.path.join(_python_site_packages(), 'libs', lib_file)
    else:
        raise Exception(f'Unsupported platform {_platform()}')
    return python_lib

def _ifport_lib():
    try:
        ifport_lib = CONFIG['build'][_platform()][_compiler_name()]
    except KeyError:
        ifport_lib = ''
    return ifport_lib

def _fix_file_permissions(path: str):
    os.chmod(path, 0o777)

def _write_lines_to_file(lines: list, name: str):
    path = os.path.join(_scripts_path(), name)
    with open(path, 'w') as file:
        for line in lines:
            if _bash_syntax():
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

def _bash_syntax():
    bash_syntax = False  # default
    if ARGS.bash_syntax:
        bash_syntax = ARGS.bash_syntax
    return bash_syntax

def _print_pcfml_wheel_dir():
    wheel_dir = CONFIG['pycfml']['dir']['wheel']
    print(wheel_dir)

def _compiler_name():
    compiler = 'gfortran'  # default
    if ARGS.compiler:
        compiler = ARGS.compiler.lower()
    return compiler

def _compiler_options():
    compiler = _compiler_name()
    mode = _compiling_mode()
    options = ''
    for build in CONFIG['build-objs']:
        if _platform() in build['platforms'] and compiler in build['compilers']:
            options = f"{build['modes']['base']}"
            if build['modes'][mode]:
                options += f" {build['modes'][mode]}"
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

def _compiler_build_exe_template():
    compiler = _compiler_name()
    template = ''
    for build in CONFIG['build-objs']:
        if _platform() in build['platforms'] and compiler in build['compilers']:
            template = build['build-exe']
            break
    return template

def _compiling_mode():
    mode = 'debug'  # default
    if ARGS.mode:
        mode = ARGS.mode.lower()
    return mode

def _compiling_progress(current: int, total: int):
    progress = round(current / total * 100)
    return progress

def _compile_obj_script_line(src_path: str,
                                   include_path: str=''):
    compiler = _compiler_name()
    options = _compiler_options()
    template_cmd = CONFIG['template']['build-obj']
    if not include_path:
        template_cmd = template_cmd.replace(' -I {INCLUDE}', '')
    else:
        template_cmd = template_cmd.replace('{INCLUDE}', include_path)
    cmd = template_cmd
    cmd = cmd.replace('{COMPILER}', compiler)
    cmd = cmd.replace('{OPTIONS}', options)
    cmd = cmd.replace('{PATH}', src_path)
    return cmd

def _compile_pycfml_shared_obj_or_dynamic_lib_script_line():
    src_name = CONFIG['pycfml']['src-name']
    shared_lib_ext = CONFIG['build']['shared-lib-ext'][_platform()]
    cfml_lib_name = CONFIG['cfml']['static-lib-name']
    cfml_dist_dir = CONFIG['cfml']['dir']['dist']
    cfml_dist_path = os.path.join(_project_path(), cfml_dist_dir)
    cfml_lib_dist_dir = CONFIG['cfml']['dir']['dist-lib']
    cfml_lib_dist_path = os.path.join(cfml_dist_path, cfml_lib_dist_dir)
    cmd = _compiler_build_shared_template()
    cmd = cmd.replace('{COMPILER}', _compiler_name())
    cmd = cmd.replace('{PATH}', src_name)
    cmd = cmd.replace('{EXT}', shared_lib_ext)
    cmd = cmd.replace('{CFML_LIB_PATH}', cfml_lib_dist_path)
    cmd = cmd.replace('{CFML_LIB_NAME}', cfml_lib_name)
    cmd = cmd.replace('{IFPORT_LIB}', _ifport_lib())
    cmd = cmd.replace('{PYTHON_LIB}', _python_lib())
    return cmd

def _compile_objs_script_lines(modules: str,
                               src_path: str,
                               include_path: str=''):
    compiler = _compiler_name()
    options = _compiler_options()
    src_ext = CONFIG['build']['src-ext']
    template_cmd = CONFIG['template']['build-obj']
    if not include_path:
        template_cmd = template_cmd.replace(' -I {INCLUDE}', '')
    else:
        template_cmd = template_cmd.replace('{INCLUDE}', include_path)
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
            cmd = template_cmd
            cmd = cmd.replace('{COMPILER}', compiler)
            cmd = cmd.replace('{OPTIONS}', options)
            cmd = cmd.replace('{PATH}', path)
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
                cmd = template_cmd
                cmd = cmd.replace('{COMPILER}', compiler)
                cmd = cmd.replace('{OPTIONS}', options)
                cmd = cmd.replace('{PATH}', path)
                #cmd = f'{cmd}&'  # start this bash command in background for parallel compilation
                lines.append(cmd)
                #if current % 11 == 0:  # do not parallelise for more than 10 compilations
                #    lines.append('wait')  # wait for all parallel bash commands to finish
            #lines.append('wait')  # wait for all parallel bash commands to finish
    return lines

def _compile_shared_objs_or_dynamic_libs_script_lines(modules: str):
    cfml_lib_name = CONFIG['cfml']['static-lib-name']
    cfml_dist_dir = CONFIG['cfml']['dir']['dist']
    cfml_dist_path = os.path.join(_project_path(), cfml_dist_dir)
    cfml_lib_dist_dir = CONFIG['cfml']['dir']['dist-lib']
    cfml_lib_dist_path = os.path.join(cfml_dist_path, cfml_lib_dist_dir)
    template_cmd = _compiler_build_shared_template()
    shared_lib_ext = CONFIG['build']['shared-lib-ext'][_platform()]
    total = _total_src_file_count(modules)
    current = 0
    lines = []
    for module in CONFIG[modules]:
        if 'main-file' in module:
            current += 1
            name = f'{module["main-file"]}'
            msg = _echo_progress_msg(current, total, f'{name}.{_obj_ext()}')
            lines.append(msg)
            cmd = template_cmd
            cmd = cmd.replace('{COMPILER}', _compiler_name())
            cmd = cmd.replace('{PATH}', name)
            cmd = cmd.replace('{EXT}', shared_lib_ext)
            cmd = cmd.replace('{CFML_LIB_PATH}', cfml_lib_dist_path)
            cmd = cmd.replace('{CFML_LIB_NAME}', cfml_lib_name)
            cmd = cmd.replace('{IFPORT_LIB}', _ifport_lib())
            cmd = cmd.replace('{PYTHON_LIB}', _python_lib())
            #lines.append(f"echo '>>>>> {cmd}'")
            lines.append(cmd)
    return lines

def _compile_executables_script_lines(section_prefix: str,
                                      src_path: str,
                                      include_path: str,
                                      lib_dir: str,
                                      lib_name: str):
    src_ext = CONFIG['build']['src-ext']
    lib_ext = CONFIG['build']['static-lib-ext'][_platform()]
    tests = f'{section_prefix}-tests'
    template_cmd = _compiler_build_exe_template()
    compiler = _compiler_name()
    options = _compiler_options()
    total = _total_src_file_count(tests)
    current = 0
    lines = []
    for test in CONFIG[tests]:
        current += 1
        dir = test["main-dir"]
        main_name = test["main-file"]
        source_name = f'{main_name}.{src_ext}'
        msg = _echo_progress_msg(current, total, f"{source_name}")
        lines.append(msg)
        source_path = os.path.join(src_path, dir, source_name)
        cmd = template_cmd
        cmd = cmd.replace('{COMPILER}', compiler)
        cmd = cmd.replace('{OPTIONS}', options)
        cmd = cmd.replace('{EXE_NAME}', main_name)
        cmd = cmd.replace('{SOURCE_PATH}', source_path)
        cmd = cmd.replace('{CFML_INCLUDE_PATH}', include_path)
        cmd = cmd.replace('{CFML_LIB_DIR}', lib_dir)
        cmd = cmd.replace('{CFML_LIB_NAME}', lib_name)
        cmd = cmd.replace('{LIB_EXT}', lib_ext)
        #lines.append(f"echo '>>>>> {cmd}'")
        lines.append(cmd)
    return lines

def parsed_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--platform",
                        default="macos",
                        choices=['macos', 'linux', 'windows'],
                        type=str.lower,
                        help="platform identifier")
    parser.add_argument("--compiler",
                        default="gfortran",
                        choices=['gfortran', 'nagfor', 'ifx', 'ifort'],
                        type=str.lower,
                        help="fortran compiler")
    parser.add_argument("--mode",
                        default="debug",
                        choices=['debug', 'release'],
                        type=str.lower,
                        help="compiling mode")
    parser.add_argument("--bash-syntax",
                        action='store_true',
                        help="force bash shell syntax")
    parser.add_argument("--print-wheel-dir",
                        action='store_true',
                        help="print pycfml wheel directory name")
    return parser.parse_args()

def loaded_pyproject():
    path = os.path.join(_project_dir(), 'pyproject.toml')
    with open(path, 'rb') as f:
        pyproject = tomllib.load(f)
    return pyproject

def loaded_config(name: str):
    path = _config_path(name)
    with open(path, 'rb') as f:
        config = tomllib.load(f)
    if _bash_syntax():
        for idx, build in enumerate(config['build-objs']):
            config['build-objs'][idx]['build-shared'] = build['build-shared'].replace('/', '-')
            config['build-objs'][idx]['build-exe'] = build['build-exe'].replace('/', '-')
            config['build-objs'][idx]['modes']['base'] = build['modes']['base'].replace('/', '-')
            config['build-objs'][idx]['modes']['debug'] = build['modes']['debug'].replace('/', '-')
            config['build-objs'][idx]['modes']['release'] = build['modes']['release'].replace('/', '-')
    return config

def clear_main_script():
    path = _main_script_path()
    with open(path, 'w') as file:
        pass

def append_to_main_script(obj: str | list):
    path = _main_script_path()
    if isinstance(obj, str):
        lines = [obj]
    elif isinstance(obj, list):
        lines = obj
    with open(path, 'a') as file:
        for line in lines:
            if _bash_syntax():
                line = line.replace('\\', '/')
            file.write(line + '\n')
    _fix_file_permissions(path)

def print_build_variables():
    lines = []
    msg = _echo_msg(f"Platform: {_platform()}")
    lines.append(msg)
    msg = _echo_msg(f"Processor: {_processor()}")
    lines.append(msg)
    msg = _echo_msg(f"Compiling mode: {_compiling_mode()}")
    lines.append(msg)
    #msg = _echo_msg(f"Compiler options '{_compiler_options()}'")
    #lines.append(msg)
    msg = _echo_msg(f"Fortran compiler: {_compiler_name()}")
    lines.append(msg)
    msg = _echo_msg(f"Python version: {_python_version_full()}")
    lines.append(msg)
    msg = _echo_msg(f"Python tag: {_python_tag()}")
    lines.append(msg)
    msg = _echo_msg(f"Python site packages: {_python_site_packages()}")
    lines.append(msg)
    msg = _echo_msg(f"Python lib: {_python_lib()}")
    lines.append(msg)
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
    project_name = CONFIG['cfml']['log-name']
    url = CONFIG['cfml']['git']['url']
    branch = CONFIG['cfml']['git']['branch']
    out_dir = CONFIG['cfml']['dir']['repo']
    out_path = os.path.abspath(out_dir)
    lines = []
    msg = _echo_msg(f"Downloading {project_name} branch '{branch}' to '{out_dir}' from '{url}'")
    lines.append(msg)
    cmd = CONFIG['template']['clone-repo']
    cmd = cmd.replace('{BRANCH}', branch)
    cmd = cmd.replace('{URL}', url)
    cmd = cmd.replace('{OUT_PATH}', out_path)
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

def rename_global_deps_file():
    repo_dir = CONFIG['cfml']['dir']['repo']
    src_ext = CONFIG['build']['src-ext']
    src_dir = CONFIG['cfml']['dir']['repo-src']
    if _platform() == 'macos':
        platform_suffix = 'MacOS'
    elif _platform() == 'linux':
        platform_suffix = 'Linux'
    elif _platform() == 'windows':
        platform_suffix = 'Windows'
    compiler = _compiler_name()
    if compiler in ['gfortran', 'nagfor']:
        compiler_suffix = 'GFOR'
    elif compiler in ['ifort', 'ifx']:
        compiler_suffix = 'IFOR'
    from_name = f'CFML_GlobalDeps_{platform_suffix}_{compiler_suffix}.{src_ext}'
    from_relpath = os.path.join(repo_dir, src_dir, from_name)
    from_abspath = os.path.join(_project_path(), from_relpath)
    to_name = f'CFML_GlobalDeps.{src_ext}'
    to_relpath = os.path.join(repo_dir, src_dir, to_name)
    to_abspath = os.path.join(_project_path(), to_relpath)
    lines = []
    msg = _echo_msg(f"Copying '{from_relpath}' to '{to_relpath}'")
    lines.append(msg)
    cmd = f'cp {from_abspath} {to_abspath}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def build_cfml_objs():
    project_name = CONFIG['cfml']['log-name']
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
    compile_lines = _compile_objs_script_lines('cfml-modules', src_path)
    lines.extend(compile_lines)
    msg = _echo_msg(f"Exiting build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {_project_path()}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def delete_renamed_global_deps_file():
    repo_dir = CONFIG['cfml']['dir']['repo']
    src_ext = CONFIG['build']['src-ext']
    src_dir = CONFIG['cfml']['dir']['repo-src']
    name = f'CFML_GlobalDeps.{src_ext}'
    relpath = os.path.join(repo_dir, src_dir, name)
    abspath = os.path.join(_project_path(), relpath)
    lines = []
    msg = _echo_msg(f"Deleting previously created '{relpath}'")
    lines.append(msg)
    cmd = f'rm {abspath}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def build_cfml_static_lib():
    lib_ext = CONFIG['build']['static-lib-ext'][_platform()]
    static_lib_prefix = CONFIG['build']['static-lib-prefix'][_platform()]
    lib_name = CONFIG['cfml']['static-lib-name']
    lib_name = f'{static_lib_prefix}{lib_name}'
    build_dir = CONFIG['cfml']['dir']['build']
    build_path = os.path.join(_project_path(), build_dir)
    lines = []
    msg = _echo_msg(f"Entering build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {build_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Creating fortran static library '{lib_name}.{lib_ext}'")
    lines.append(msg)
    cmd = CONFIG['template']['build-static'][_platform()]
    cmd = cmd.replace('{LIB}', lib_name)
    cmd = cmd.replace('{OBJ_EXT}', _obj_ext())
    lines.append(cmd)
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

def copy_built_to_cfml_dist():
    lib_ext = CONFIG['build']['static-lib-ext'][_platform()]
    static_lib_prefix = CONFIG['build']['static-lib-prefix'][_platform()]
    lib_name = CONFIG['cfml']['static-lib-name']
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
    msg = _echo_msg(f"Copying built lib '{lib_name}.{lib_ext}' to dist dir '{dist_dir}/{lib_dist_dir}'")
    lines.append(msg)
    from_path = os.path.join(build_path, f'{lib_name}.{lib_ext}')
    cmd = f'cp {from_path} {lib_dist_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Copying built modules to dist dir '{dist_dir}/{include_dist_dir}'")
    lines.append(msg)
    from_path = os.path.join(build_path, '*.*mod')
    cmd = f'cp {from_path} {include_dist_path}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def build_cfml_test_programs():
    project_name = CONFIG['cfml']['log-name']
    repo_dir = CONFIG['cfml']['dir']['repo']
    src_dir = CONFIG['cfml']['dir']['repo-tests']
    src_path = os.path.join(_project_path(), repo_dir, src_dir)
    build_dir = os.path.join('tests', 'functional_tests', 'cfml')
    build_path = os.path.join(_project_path(), build_dir)
    dist_dir = CONFIG['cfml']['dir']['dist']
    include_dir = CONFIG['cfml']['dir']['dist-include']
    include_path = os.path.join(_project_path(), dist_dir, include_dir)
    lib_dir = CONFIG['cfml']['dir']['dist-lib']
    lib_path = os.path.join(_project_path(), dist_dir, lib_dir)
    lib_name = CONFIG['cfml']['static-lib-name']
    lines = []
    msg = _echo_msg(f"Entering build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {build_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Building test programs for {project_name}:")
    lines.append(msg)
    compile_lines = _compile_executables_script_lines('cfml', src_path, include_path, lib_path, lib_name)
    lines.extend(compile_lines)
    msg = _echo_msg(f"Exiting build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {_project_path()}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def run_cfml_functional_tests_no_benchmarks():
    relpath = os.path.join('tests', 'functional_tests', 'cfml')
    abspath = os.path.join(_project_path(), relpath)
    lines = []
    msg = _echo_msg(f"Running functional tests from '{relpath}'")
    lines.append(msg)
    cmd = CONFIG['template']['run-tests']
    cmd = cmd.replace('{PATH}', abspath)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def run_cfml_functional_tests_with_benchmarks():
    relpath = os.path.join('tests', 'functional_tests', 'cfml')
    abspath = os.path.join(_project_path(), relpath)
    lines = []
    msg = _echo_msg(f"Running functional tests with benchmarks from '{relpath}'")
    lines.append(msg)
    cmd = CONFIG['template']['run-benchmarks']['base']
    if _github_branch() == 'master':
        cmd += ' ' + CONFIG['template']['run-benchmarks']['master-branch']
    else:
        cmd += ' ' + CONFIG['template']['run-benchmarks']['non-master-branch']
    cmd = cmd.replace('{PATH}', abspath)
    if _github_actions():
        cmd = cmd.replace('{RUNNER}', 'github')
    else:
        cmd = cmd.replace('{RUNNER}', 'local')
    cmd = cmd.replace('{COMPILER}', _compiler_name())
    cmd = cmd.replace('{PROCESSOR}', _processor())
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
    project_name = CONFIG['pycfml']['log-name']
    url = CONFIG['pycfml']['git']['url']
    branch = CONFIG['pycfml']['git']['branch']
    out_dir = CONFIG['pycfml']['dir']['repo']
    out_path = os.path.abspath(out_dir)
    lines = []
    msg = _echo_msg(f"Downloading {project_name} branch '{branch}' to '{out_dir}' from '{url}'")
    lines.append(msg)
    cmd = CONFIG['template']['clone-repo']
    cmd = cmd.replace('{BRANCH}', branch)
    cmd = cmd.replace('{URL}', url)
    cmd = cmd.replace('{OUT_PATH}', out_path)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def copy_powder_mod_to_pycfml_repo():
    cfml_project_name = CONFIG['cfml']['log-name']
    cfml_repo_dir = CONFIG['cfml']['dir']['repo']
    cfml_repo_path = os.path.join(_project_path(), cfml_repo_dir)
    pycfml_project_name = CONFIG['pycfml']['log-name']
    pycfml_repo_dir = CONFIG['pycfml']['dir']['repo']
    pycfml_src_dir = CONFIG['pycfml']['dir']['repo-src']
    pycfml_src_path = os.path.join(_project_path(), pycfml_repo_dir, pycfml_src_dir)
    src_ext = CONFIG['build']['src-ext']
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

def create_pycfml_wraps_src():
    project_name = CONFIG['cfml']['log-name']
    repo_dir = CONFIG['cfml']['dir']['repo']
    apigen_dir = CONFIG['cfml']['apigen-dir']
    apigen_dir = os.path.join(repo_dir, *apigen_dir.split('/'))
    apigen_path = os.path.join(_project_path(), apigen_dir)
    apigen_file = CONFIG['cfml']['apigen-file']
    lines = []
    msg = _echo_msg(f"Entering apigen dir '{apigen_dir}'")
    lines.append(msg)
    cmd = f'cd {apigen_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Creating {project_name} wraps")
    lines.append(msg)
    cmd = CONFIG['template']['run-python']
    cmd = cmd.replace('{PATH}', apigen_file)
    lines.append(cmd)
    msg = _echo_msg(f"Exiting build dir '{apigen_dir}'")
    lines.append(msg)
    cmd = f'cd {_project_path()}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def build_pycfml_wraps_objs():
    project_name = CONFIG['cfml']['log-name']
    repo_dir = CONFIG['cfml']['dir']['repo']
    wraps_dir = CONFIG['cfml']['dir']['repo-wraps']
    src_path = os.path.join(_project_path(), repo_dir, *wraps_dir.split('/'))
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
    msg = _echo_msg(f"Building fortran objects for {project_name} wraps")
    lines.append(msg)
    compile_lines = _compile_objs_script_lines('cfml-wraps', src_path, include_dist_path)
    lines.extend(compile_lines)
    msg = _echo_msg(f"Exiting build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {_project_path()}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def build_pycfml_lib_obj():
    project_name = CONFIG['pycfml']['log-name']
    repo_dir = CONFIG['cfml']['dir']['repo']
    wraps_dir = CONFIG['cfml']['dir']['repo-wraps']
    src_ext = CONFIG['build']['src-ext']
    pycfml_src_name = CONFIG['pycfml']['src-name']
    pycfml_src_file = f'{pycfml_src_name}.{src_ext}'
    src_path = os.path.join(_project_path(), repo_dir, *wraps_dir.split('/'), pycfml_src_file)
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
    msg = _echo_msg(f"Building fortran object of {project_name} lib")
    lines.append(msg)
    compile_line = _compile_obj_script_line(src_path, include_dist_path)
    lines.append(compile_line)
    msg = _echo_msg(f"Exiting build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {_project_path()}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def build_pycfml_shared_objs_or_dynamic_libs():
    project_name = CONFIG['pycfml']['log-name']
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






def build_pycfml_shared_obj_or_dynamic_lib():
    project_name = CONFIG['pycfml']['log-name']
    build_dir = CONFIG['pycfml']['dir']['build']
    build_path = os.path.join(_project_path(), build_dir)
    lib_name = CONFIG['pycfml']['src-name']  # NED FIX: use CONFIG['pycfml']['dynamic-lib-name']
    lib_ext = CONFIG['build']['shared-lib-ext'][_platform()]

    lines = []
    msg = _echo_msg(f"Entering build dir '{build_dir}'")
    lines.append(msg)

    #lines.append(f'ls -l {build_path}')

    cmd = f'cd {build_path}'
    lines.append(cmd)
    msg = _echo_msg(f"Building fortran shared obj or dynamic lib '{lib_name}.{lib_ext}'")

    lines.append(msg)
    compile_line = _compile_pycfml_shared_obj_or_dynamic_lib_script_line()
    lines.append(compile_line)
    msg = _echo_msg(f"Exiting build dir '{build_dir}'")
    lines.append(msg)
    cmd = f'cd {_project_path()}'
    lines.append(cmd)

    #lines.append(f'ls -l {build_path}')

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

def copy_built_to_pycfml_dist():
    shared_lib_ext = CONFIG['build']['shared-lib-ext'][_platform()]
    project_name = CONFIG['pycfml']['log-name']
    build_dir = CONFIG['pycfml']['dir']['build']
    build_path = os.path.join(_project_path(), build_dir)
    dist_dir = CONFIG['pycfml']['dir']['dist']
    package_dir = CONFIG['pycfml']['dir']['dist-package']
    package_relpath = os.path.join(dist_dir, package_dir)
    package_abspath = os.path.join(_project_path(), dist_dir, package_dir)
    lines = []
    msg = _echo_msg(f"Copying built {project_name} shared objects or dynamic libs to '{package_relpath}'")
    lines.append(msg)
    from_path = os.path.join(build_path, f'*.{shared_lib_ext}')
    cmd = f'cp {from_path} {package_abspath}'
    lines.append(cmd)

    #lines.append(f"ls -l {os.path.join(_project_path(), CONFIG['pycfml']['dir']['dist']), CONFIG['pycfml']['dir']['dist-package'])}")

    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def change_runpath_for_built_pycfml():
    # Tried to set rpath to $ORIGIN (with -Wl,-rpath,'$ORIGIN') during the build
    # shared objects step (CONFIG['build-shared']), but it didn't help :(
    # Ubuntu usage examples:
    # sudo find / -iname "libif*"
    # ls -l pycrysfml08_dist/pycrysfml08
    # patchelf --print-rpath pycrysfml08_dist/pycrysfml08/py_cfml_metrics.so
    # patchelf --set-rpath '$ORIGIN' pycrysfml08_dist/pycrysfml08/py_cfml_metrics.so
    # patchelf --print-rpath pycrysfml08_dist/pycrysfml08/py_cfml_metrics.so
    # patchelf --no-default-lib pycrysfml08_dist/pycrysfml08/py_cfml_metrics.so
    # ldd pycrysfml08_dist/pycrysfml08/py_cfml_metrics.so
    # ls -l /opt/hostedtoolcache/Python/3.11.8/x64/lib/python3.11/site-packages/pycrysfml08
    # ldd /opt/hostedtoolcache/Python/3.11.8/x64/lib/python3.11/site-packages/pycrysfml08/py_cfml_metrics.so
    # macOS usage example:
    # sudo find / -iname "libif*"
    # ls -l pycrysfml08_dist/pycrysfml08
    # install_name_tool -rpath /opt/intel/oneapi/compiler/2023.2.0/mac/bin/intel64/../../compiler/lib @loader_path pycrysfml08_dist/pycrysfml08/py_cfml_metrics.so
    # install_name_tool -delete_rpath /usr/local/Cellar/gcc/13.2.0/lib/gcc/current pycrysfml08_dist/pycrysfml08/py_cfml_metrics.so
    # install_name_tool -change /usr/local/opt/gcc/lib/gcc/current/libgfortran.5.dylib @rpath/libgfortran.5.dylib pycrysfml08_dist/pycrysfml08/py_cfml_metrics.so
    # otool -L pycrysfml08_dist/pycrysfml08/py_cfml_metrics.so
    # otool -l pycrysfml08_dist/pycrysfml08/py_cfml_metrics.so | grep RPATH -A2
    try:
        rpaths = CONFIG['build']['rpaths'][_platform()][_processor()][_compiler_name()]
    except KeyError:
        msg = _echo_msg(f"No change of runtime paths are needed for platform '{_platform()} ({_processor()})' and compiler '{_compiler_name()}'")
        lines = [msg]
        script_name = f'{sys._getframe().f_code.co_name}.sh'
        _write_lines_to_file(lines, script_name)
        append_to_main_script(lines)
        return
    project_name = CONFIG['pycfml']['log-name']
    shared_lib_ext = CONFIG['build']['shared-lib-ext'][_platform()]
    dist_dir = CONFIG['pycfml']['dir']['dist']
    package_dir = CONFIG['pycfml']['dir']['dist-package']
    package_relpath = os.path.join(dist_dir, package_dir)
    package_abspath = os.path.join(_project_path(), dist_dir, package_dir)
    #total = 1
    #current = 0
    lines = []
    if _platform() == 'linux':
        set_rpath_template_cmd = CONFIG['template']['rpath']['set'][_platform()]
        no_default_lib_template_cmd = CONFIG['template']['no-default-lib'][_platform()]
        msg = _echo_msg(f"Changing runpath(s) for built {project_name} shared objects")
        lines.append(msg)
        name = CONFIG['pycfml']['src-name']
        path = os.path.join(package_abspath, name)
        for rpath in rpaths:
            #current += 1
            #name = f'{module["main-file"]}'
            #path = os.path.join(package_abspath, name)
            #msg = _echo_progress_msg(current, total, f'{name}.{shared_lib_ext}')
            msg = _echo_msg(f"Changing runpath for {name}.{shared_lib_ext} from {rpath['old']} to {rpath['new']}")
            lines.append(msg)
            cmd = set_rpath_template_cmd
            cmd = cmd.replace('{NEW}', rpath['new'])
            cmd = cmd.replace('{PATH}', path)
            cmd = cmd.replace('{EXT}', shared_lib_ext)
            lines.append(cmd)
            cmd = no_default_lib_template_cmd
            cmd = cmd.replace('{PATH}', path)
            cmd = cmd.replace('{EXT}', shared_lib_ext)
            lines.append(cmd)
    elif _platform() == 'macos':
        try:
            dependent_libs = CONFIG['build']['dependent-libs'][_platform()][_processor()][_compiler_name()]
            change_lib_template_cmd = CONFIG['template']['dependent-lib']['change'][_platform()]
        except KeyError:
            dependent_libs = []
        delete_rpath_template_cmd = CONFIG['template']['rpath']['delete'][_platform()]
        change_rpath_template_cmd = CONFIG['template']['rpath']['change'][_platform()]
        msg = _echo_msg(f"Changing runpath(s) for built {project_name} shared objects")
        lines.append(msg)
        for module in [CONFIG['pycfml']['src-name']]:
            if 'main-file' in module:
                current += 1
                name = f'{module["main-file"]}'
                path = os.path.join(package_abspath, name)
                msg = _echo_progress_msg(current, total, f'{name}.{shared_lib_ext}')
                lines.append(msg)
                for rpath in rpaths:
                    if rpath['new'] == '':  # delete this rpath
                        cmd = delete_rpath_template_cmd
                        cmd = cmd.replace('{OLD}', rpath['old'])
                        cmd = cmd.replace('{PATH}', path)
                        cmd = cmd.replace('{EXT}', shared_lib_ext)
                    else:  # change this rpath
                        cmd = change_rpath_template_cmd
                        cmd = cmd.replace('{OLD}', rpath['old'])
                        cmd = cmd.replace('{NEW}', rpath['new'])
                        cmd = cmd.replace('{PATH}', path)
                        cmd = cmd.replace('{EXT}', shared_lib_ext)
                    lines.append(cmd)
                for lib in dependent_libs:
                    cmd = change_lib_template_cmd
                    cmd = cmd.replace('{OLD}', lib['old'])
                    cmd = cmd.replace('{NEW}', lib['new'])
                    cmd = cmd.replace('{PATH}', path)
                    cmd = cmd.replace('{EXT}', shared_lib_ext)
                    lines.append(cmd)
    else:
        msg = _echo_msg(f"Changing runpath is not needed for platform '{_platform()}'")
        lines.append(msg)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def copy_extra_libs_to_pycfml_dist():
    try:
        extra_libs = CONFIG['build']['extra-libs'][_platform()][_processor()][_compiler_name()]
    except KeyError:
        msg = _echo_msg(f"No extra libraries are needed for platform '{_platform()}' and compiler '{_compiler_name()}'")
        lines = [msg]
        script_name = f'{sys._getframe().f_code.co_name}.sh'
        _write_lines_to_file(lines, script_name)
        append_to_main_script(lines)
        return
    dist_dir = CONFIG['pycfml']['dir']['dist']
    package_dir = CONFIG['pycfml']['dir']['dist-package']
    package_relpath = os.path.join(dist_dir, package_dir)
    package_abspath = os.path.join(_project_path(), package_relpath)
    lines = []
    for lib_path in extra_libs:
        msg = _echo_msg(f"Copying {lib_path} to dist dir '{package_relpath}'")
        lines.append(msg)
        cmd = f'cp {lib_path} {package_abspath}'
        lines.append(cmd)

    #lines.append(f"ls -l {os.path.join(_project_path(), CONFIG['pycfml']['dir']['dist']), CONFIG['pycfml']['dir']['dist-package'])}")

    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def copy_py_api_files_to_pycfml_dist():
    project_name = CONFIG['pycfml']['log-name']
    repo_dir = CONFIG['cfml']['dir']['repo']
    dist_dir = CONFIG['pycfml']['dir']['dist']
    from_dir = os.path.join(repo_dir, 'build', 'Python_API', '*.py')
    from_path = os.path.join(_project_path(), from_dir)
    package_dir = CONFIG['pycfml']['dir']['dist-package']
    package_relpath = os.path.join(dist_dir, package_dir)
    package_abspath = os.path.join(_project_path(), package_relpath)
    lines = []
    msg = _echo_msg(f"Copying {project_name} python api files from '{from_dir}' to dist dir '{package_relpath}'")
    lines.append(msg)
    cmd = f'cp {from_path} {package_abspath}'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def copy_init_file_to_pycfml_dist():
    project_name = CONFIG['pycfml']['log-name']
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

    #lines.append(f"ls -l {os.path.join(_project_path(), CONFIG['pycfml']['dir']['dist']), CONFIG['pycfml']['dir']['dist-package'])}")

    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def copy_cfml_databases_to_pycfml_dist():
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

    #lines.append(f"ls -l {os.path.join(_project_path(), CONFIG['pycfml']['dir']['dist']), CONFIG['pycfml']['dir']['dist-package'])}")

    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def validate_pyproject_toml():
    lines = []
    msg = _echo_msg(f"Validating pyproject.toml")
    lines.append(msg)
    cmd = 'validate-pyproject pyproject.toml'
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def create_pycfml_python_wheel():
    project_name = CONFIG['pycfml']['log-name']
    wheel_dir = CONFIG['pycfml']['dir']['wheel']
    wheel_path = os.path.join(_project_path(), wheel_dir)
    lines = []
    msg = _echo_msg(f"Creating '{project_name}' python wheel in '{wheel_dir}'")
    lines.append(msg)

    #lines.append(f"ls -l {os.path.join(_project_path(), CONFIG['pycfml']['dir']['dist']), CONFIG['pycfml']['dir']['dist-package'])}")

    cmd = CONFIG['template']['build-wheel']
    cmd = cmd.replace('{PATH}', wheel_path)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def rename_pycfml_python_wheel():
    project_name = CONFIG['pycfml']['log-name']
    pycfml_package_dir = CONFIG['pycfml']['dir']['dist-package']
    dist_package_version = PYPROJECT['project']['version']
    initial_wheel_name = f'{pycfml_package_dir}-{dist_package_version}-py3-none-any.whl'
    wheel_dir = CONFIG['pycfml']['dir']['wheel']
    wheel_relpath = os.path.join(wheel_dir, initial_wheel_name)
    wheel_abspath = os.path.join(_project_path(), wheel_relpath)
    lines = []
    msg = _echo_msg(f"Renaming '{project_name}' python wheel from '{wheel_relpath}'")
    lines.append(msg)
    cmd = CONFIG['template']['rename-wheel']
    cmd = cmd.replace('{PYTHON_TAG}', _python_tag())  # https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/
    cmd = cmd.replace('{PLATFORM_TAG}', _platform_tag())
    cmd = cmd.replace('{PATH}', wheel_abspath)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    #append_to_main_script(lines)

def install_pycfml_from_wheel():
    project_name = CONFIG['pycfml']['log-name']
    package_name = CONFIG['pycfml']['dir']['dist-package']
    wheel_dir = CONFIG['pycfml']['dir']['wheel']
    wheel_path = os.path.join(_project_path(), wheel_dir)
    lines = []
    msg = _echo_msg(f"Installing '{project_name}' python wheel from '{wheel_dir}'")
    lines.append(msg)
    cmd = CONFIG['template']['install-wheel']
    cmd = cmd.replace('{PACKAGE}', package_name)
    cmd = cmd.replace('{PATH}', wheel_path)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def run_pycfml_unit_tests():
    relpath = os.path.join('tests', 'unit_tests', 'pycfml')
    abspath = os.path.join(_project_path(), relpath)
    lines = []
    msg = _echo_msg(f"Running unit tests from '{relpath}'")
    lines.append(msg)
    cmd = CONFIG['template']['run-tests']
    cmd = cmd.replace('{PATH}', abspath)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def run_powder_mod_tests():
    relpath = os.path.join('tests', 'functional_tests', 'pycfml')
    abspath = os.path.join(_project_path(), relpath)
    lines = []
    msg = _echo_msg(f"Running powder_mod tests from '{relpath}'")
    lines.append(msg)
    cmd = CONFIG['template']['run-tests']
    cmd = cmd.replace('{PATH}', abspath)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

def run_powder_mod_main():
    relpath = os.path.join('tests', 'functional_tests', 'pycfml', 'test__powder_mod.py')
    abspath = os.path.join(_project_path(), relpath)
    lines = []
    msg = _echo_msg(f"Running powder_mod main from '{relpath}'")
    lines.append(msg)
    cmd = CONFIG['template']['run-python']
    cmd = cmd.replace('{PATH}', abspath)
    lines.append(cmd)
    script_name = f'{sys._getframe().f_code.co_name}.sh'
    _write_lines_to_file(lines, script_name)
    append_to_main_script(lines)

if __name__ == '__main__':
    ARGS = parsed_args()
    PYPROJECT = loaded_pyproject()
    CONFIG = loaded_config('scripts.toml')

    if ARGS.print_wheel_dir:  # NEED FIX. Maybe save extras to toml as in EDA?
        _print_pcfml_wheel_dir()
        exit(0)

    cfml_project_name = CONFIG['cfml']['log-name']
    pycfml_project_name = CONFIG['pycfml']['log-name']

    clear_main_script()

    headers = _echo_header(f"Info")
    append_to_main_script(headers)
    print_build_variables()

    headers = _echo_header(f"Creating directories")
    append_to_main_script(headers)
    create_cfml_repo_dir()
    create_cfml_build_dir()
    create_cfml_dist_dir()
    create_pycfml_repo_dir()
    create_pycfml_build_dir()
    create_pycfml_dist_dir()

    headers = _echo_header(f"Downloading repositories")
    append_to_main_script(headers)
    download_cfml_repo()
    download_pycfml_repo()

    headers = _echo_header(f"Creating {cfml_project_name} static library")
    append_to_main_script(headers)
    rename_global_deps_file()
    build_cfml_objs()
    delete_renamed_global_deps_file()
    build_cfml_static_lib()
    copy_built_to_cfml_dist()

    headers = _echo_header(f"Creating and running {cfml_project_name} test programs")
    append_to_main_script(headers)
    build_cfml_test_programs()
    run_cfml_functional_tests_no_benchmarks()
    #run_cfml_functional_tests_with_benchmarks()

    headers = _echo_header(f"Creating {pycfml_project_name} shared object / dynamic library")
    append_to_main_script(headers)
    create_pycfml_wraps_src()
    build_pycfml_wraps_objs()
    build_pycfml_lib_obj()
    build_pycfml_shared_obj_or_dynamic_lib()
    copy_built_to_pycfml_dist()
    change_runpath_for_built_pycfml()

    headers = _echo_header(f"Creating {pycfml_project_name} python package wheel")
    append_to_main_script(headers)
    copy_extra_libs_to_pycfml_dist()
    copy_py_api_files_to_pycfml_dist()
    copy_init_file_to_pycfml_dist()
    copy_cfml_databases_to_pycfml_dist()
    validate_pyproject_toml()
    create_pycfml_python_wheel()
    rename_pycfml_python_wheel()

    headers = _echo_header(f"Installing {pycfml_project_name} from python wheel")
    append_to_main_script(headers)
    install_pycfml_from_wheel()

    headers = _echo_header(f"Running {pycfml_project_name} tests")
    append_to_main_script(headers)
    run_pycfml_unit_tests()
    run_powder_mod_tests()
    run_powder_mod_main()
