[app]

# (str) Title of your application
title = Removedor de Marca d'Água

# (str) Package name
package.name = removedormarcadagua

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code path
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"'](.*)['"']
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = python3,kivy,opencv-python,moviepy,numpy

# (str) Custom source folders for components
# source.include_source_exts = py

# (list) Import files to be imported
# source.include_py = sitecustomize.py

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

# (str) Path to use for Mac bundle, default is a relative path to bundles dir under build dir
# osx.bundle_path = ./build/Application.app

# (str) Name of the .app
# osx.app_name = MyApplication

# (str) Version of the application to be bundled
# osx.app_version = 0.1

# (str) Bundle build number
# osx.build_number = 1

# (str) Bundle identifier
# osx.bundle_identifier = org.test.myapplication

#
# iOS Specific
#

# (str) Path to use for iOS bundle, default is a relative path to bundles dir under build dir
# ios.bundle_path = ./build/Application.app

# (str) Name of the application to be bundled
# ios.app_name = MyApplication

# (str) Version of the application to be bundled
# ios.app_version = 0.1

# (str) Bundle identifier
# ios.bundle_identifier = org.test.myapplication

# (str) Bundle version
# ios.build_number = 1

# (str) Icon of the application
# ios.icon_filename = %(source.dir)s/data/icon.png

# (list) List of entitlements
# ios.entitlements = []

# (bool) Use a wildcard for provisioning profile
# ios.codesign.allow_provisioning_profile_wildcard = True

# (str) Name of the certificate to use for signing the debug version
# ios.codesign.debug = iPhone Developer: <Name> (<Identifier>)

# (str) Name of the certificate to use for signing the release version
# ios.codesign.release = iPhone Distribution: <Name> (<Identifier>)

#
# Android Specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA

# (int) Android API to use
#android.api = 27

# (int) Minimum API required
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 19b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip updating buildozer spec file
#android.skip_update = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (list) List of Java .jar files to add to the libs so the pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add (currently works only with sdl2_gradle
# bootstrap)
#android.add_aars =

# (list) Gradle dependencies to add (currently works only with sdl2_gradle
# bootstrap)
#android.gradle_dependencies =

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (bool) OUYA Console specific
#android.ouya = False

# (str) Filename of OUYA Console icon
#ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (list) Android additionnal libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android additionnal java libraries
#android.add_java_libs = libs/android/*.jar

# (list) Android additionnal aar libraries
#android.add_aar_libs = libs/android/*.aar

# (list) Gradle dependencies to add in the build.gradle
#android.gradle_dependencies =

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1