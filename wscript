# hamt_c/wscript

BASENAME = 'hamt'
LIBNAME  = BASENAME + '_c_lib'

# waf combines these two to get the archive name
APPNAME = BASENAME + '_c'
VERSION = '0.1.2'

top     = '.'
out     = "build"

def options(ctx):
    ctx.load('compiler_c')
    ctx.add_option('--shared', action='store_true',
        help='build static library')
    ctx.add_option('--static', action='store_true',
        help='build static library')

def configure(ctx):
    ctx.load('compiler_c')
    # ctx.env.append_value('CFLAGS', ['-g'])

def build(ctx):
    if ctx.options.shared:
        ctx.env.append_value('LINKFLAGS', ['-Lbuild/lib' + LIBNAME + '.so'])
        # this isn't found with or without the .so  XXX
        ctx.env.append_value('LIB', ['lib' + LIBNAME + '.so'])
        ctx.shlib(source='src/version.c', target=LIBNAME,
            includes=['include'], cxxflags='-g -Wall -O0')
    else:
        # build a static library by default
        ctx.stlib(source='src/version.c', target=LIBNAME,
            includes=['include'], cxxflags='-g -Wall -O0')

    ctx.program(source='src/main.c', target=APPNAME, includes='include',
        use=LIBNAME)
