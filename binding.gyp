{
  "targets": [
    {
      "target_name": "seed-node-native-module",
      "sources": ["src/seed-node-native-module.cc"],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}