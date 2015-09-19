#coding=utf-8

import shutil
import os
import sys

"""mod template path
"""
SRC='/home/zeek/.local/share/Steam/steamapps/common/dont_starve/mods/workshop-361213674/'

"""my default ds tools mod path
"""
DST='/home/zeek/Work/ds_mod_tools-master/build/dont_starve/mods/'

"""autocompiler tool path
"""
TOOL='/home/zeek/Work/ds_mod_tools-master/build/linux/mod_tools/autocompiler'

"""ds mod root path
"""
DS_MOD_PATH='/home/zeek/.local/share/Steam/steamapps/common/dont_starve/mods/'

"""copy file to current directory
"""
def copy_dir(dst=DST, src=SRC):
    if os.path.isdir(src):
        try:
            shutil.copytree(src, dst)
        except OSError, e:
            return 'file exists'
    else:
        return "it's not a dir"

"""rename file and the file content
"""
def rename(new_name, src=DST):
    src += new_name
    if os.path.isdir(src):
        os.remove(os.path.join(src, 'anim/esctemplate.zip'))

        os.rename(os.path.join(src, 'bigportraits/esctemplate.png'),
           os.path.join(src, 'bigportraits/', new_name+'.png'))
        os.remove(os.path.join(src, 'bigportraits/esctemplate.tex'))
        os.remove(os.path.join(src, 'bigportraits/esctemplate.xml'))

        os.rename(os.path.join(src, 'exported/esctemplate'),
            os.path.join(src, 'exported/', new_name))
        os.rename(os.path.join(src, 'exported/esctemplate_cleared'),
            os.path.join(src, 'exported/', new_name+'_cleared'))
        os.rename(os.path.join(src, 'exported/'+new_name+'/esctemplate.scml'),
             os.path.join(src, 'exported/'+new_name+'/', new_name+'.scml'))
        os.remove(os.path.join(src, 'exported/'+new_name+'/esctemplate.zip'))

        os.rename(os.path.join(src, 'images/map_icons/esctemplate.png'),
              os.path.join(src, 'images/map_icons/', new_name+'.png'))
        os.remove(os.path.join(src, 'images/map_icons/esctemplate.tex'))
        os.remove(os.path.join(src, 'images/map_icons/esctemplate.xml'))

        os.rename(os.path.join(src, 'images/saveslot_portraits/esctemplate.png'),
              os.path.join(src, 'images/saveslot_portraits/', new_name+'.png'))
        os.remove(os.path.join(src, 'images/saveslot_portraits/esctemplate.tex'))
        os.remove(os.path.join(src, 'images/saveslot_portraits/esctemplate.xml'))

        os.rename(os.path.join(src, 'images/selectscreen_portraits/esctemplate.png'),
              os.path.join(src, 'images/selectscreen_portraits/', new_name+'.png'))
        os.remove(os.path.join(src, 'images/selectscreen_portraits/esctemplate.tex'))
        os.remove(os.path.join(src, 'images/selectscreen_portraits/esctemplate.xml'))

        os.rename(os.path.join(src, 'images/selectscreen_portraits/esctemplate_silho.png'),
              os.path.join(src, 'images/selectscreen_portraits/', new_name+'_silho'+'.png'))
        os.remove(os.path.join(src, 'images/selectscreen_portraits/esctemplate_silho.tex'))
        os.remove(os.path.join(src, 'images/selectscreen_portraits/esctemplate_silho.xml'))

        os.rename(os.path.join(src, 'scripts/prefabs/esctemplate.lua'),
              os.path.join(src, 'scripts/prefabs/', new_name+'.lua'))
        os.rename(os.path.join(src, 'scripts/speech_esctemplate.lua'),
              os.path.join(src, 'scripts/','speech_'+new_name+'.lua'))
        with open(os.path.join(src, 'scripts/prefabs/', new_name+'.lua'), 'r') as f:
            content = f.read()
            replaced_content = content.replace('esctemplate', new_name)
        with open(os.path.join(src, 'scripts/prefabs/', new_name+'.lua'), 'w') as f:
            f.write(replaced_content)

        with open(os.path.join(src, 'modmain.lua'), 'r') as f:
            content = f.read()
            replaced_content = content.replace('esctemplate', new_name).replace('ESCTEMPLATE', new_name.upper())
        with open(os.path.join(src, 'modmain.lua'), 'w') as f:
            f.write(replaced_content)

        with open(os.path.join(src, 'modinfo.lua'), 'r') as f:
            content = f.read()
            replaced_content = content.replace('Extended Sample Character', new_name)
        with open(os.path.join(src, 'modinfo.lua'), 'w') as f:
            f.write(replaced_content)

"""run the ds autocompiler
"""
def auto_compiler():
    path=os.path.relpath(TOOL, os.getcwd())
    os.system('./'+path)

"""delete the original ds mod file
"""
def del_dir(dst):
    if os.path.isdir(dst):
        shutil.rmtree(dst)

if __name__ == '__main__':
    # empty
    if len(sys.argv) < 2:
        print 'use -h get help'
        exit()

    # help
    if sys.argv[1] == '-h':
        print 'use -i to initalize mod'
        print 'use -e to finish editing mod'
        exit()

    character_name = raw_input('enter your character name:')

    # init
    if sys.argv[1] == '-i':
        copy_dir(DST+character_name)
        rename(character_name)
        auto_compiler()
        copy_dir(DS_MOD_PATH+character_name, DST+character_name)

    # edit
    if sys.argv[1] == '-e':
        auto_compiler()
        del_dir(DS_MOD_PATH+character_name)
        copy_dir(DS_MOD_PATH+character_name, DST+character_name)


