[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.zz5258642

version = 0.2

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,otf
source.include_patterns = fonts/*

requirements = python3,kivy

orientation = portrait
fullscreen = 1

# 你要的：32位/64位会由 workflow 自动改成单个 arch 分别构建
android.archs = arm64-v8a

android.api = 33
android.minapi = 21

# 常用权限（可按需删）
android.permissions = INTERNET

# 可选：开启日志更清晰
android.logcat_filters = *:S python:D
