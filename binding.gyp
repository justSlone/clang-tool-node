{
  "targets": [
    {
      "target_name": "clang_tool",
      "sources": [
        "src/clang/clang_diagnostic.cpp",
        "src/clang/clang_ressource_usage.cpp",
        "src/clang/clang_tool.cpp",
        "src/clang/clang_translation_unit.cpp",
        "src/clang/clang_translation_unit_cache.cpp",
        "src/clang/sha1.cpp",
        "src/bindings.cpp"
      ],
      "cflags_cc": [
        "-O3",
        "-fomit-frame-pointer",
        "-std=c++11",
        "-Wall",
        "-Wno-unused-variable",
        "-Wno-unused-function"
      ],
      "include_dirs": [
        "/usr/local/llvm39/include",
        "/usr/local/llvm38/include",
        "/usr/local/llvm37/include",
        "/usr/local/llvm36/include",
        "/usr/local/llvm35/include",
        "/usr/local/llvm34/include",
        "/usr/local/include",
        "/usr/local/include/llvm",
        "/usr/lib",
        "/usr/lib64",
        "/usr/lib/llvm",
        "/usr/lib64/llvm",
        "/usr/lib/llvm-3.9/include",
        "/usr/lib/llvm-3.8/include",
        "/usr/lib/llvm-3.7/include",
        "/usr/lib/llvm-3.6/include",
        "/usr/lib/llvm-3.5/include",
        "/opt/local/libexec/llvm-3.9/include",
        "/opt/local/libexec/llvm-3.8/include",
        "/opt/local/libexec/llvm-3.7/include",
        "/usr/include",
        "/usr/include/llvm",
        '<!(node -e "require(\'nan\')")',
        "src"
      ],
      "libraries": [
        "-lclang",

        "-L/usr/local/llvm39/lib",
        "-L/usr/local/llvm38/lib",
        "-L/usr/local/llvm37/lib",
        "-L/usr/local/llvm36/lib",
        "-L/usr/local/llvm35/lib",
        "-L/usr/local/llvm34/lib",
        "-L/usr/lib/llvm-3.9/lib",
        "-L/usr/lib/llvm-3.8/lib",
        "-L/usr/lib/llvm-3.7/lib",
        "-L/usr/lib/llvm-3.6/lib",
        "-L/usr/lib/llvm-3.5/lib",
        "-L/usr/lib/llvm-3.4/lib",
        "-L/usr/lib/x86_64-linux-gnu/",
        "-L/usr/lib/i386-linux-gnu/",
        "-L/opt/local/libexec/llvm-3.9/lib",
        "-L/opt/local/libexec/llvm-3.8/lib",
        "-L/opt/local/libexec/llvm-3.7/lib",
        "-L/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib"
      ],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          "-stdlib=libc++",
          "-mmacosx-version-min=10.7",
          "-O3",
          "-fomit-frame-pointer",
          "-std=c++11",
          "-Wall",
          "-Wno-unused-variable",
          "-Wno-unused-function",
        ]
      }
    }
  ]
}
