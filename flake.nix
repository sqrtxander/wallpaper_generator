{
  description = "Wallpaper generator";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";
  };
  outputs = {
    self,
    nixpkgs,
  }: let
    systems = [
      "x86_64-linux"
      "aarch64-linux"
    ];
    forAllSystems = nixpkgs.lib.genAttrs systems;
  in {
    packages = forAllSystems (system: let
      pkgs = import nixpkgs {inherit system;};
      python = pkgs.python313;
      wallpaper-generator = python.pkgs.buildPythonApplication {
        pname = "wallpaper-generator";
        version = "0.1.0";
        src = self;
        pyproject = true;
        build-system = with python.pkgs; [
          setuptools
        ];
        dependencies = with python.pkgs; [
          numpy
          pillow
          scipy
        ];
        meta = {
          description = "Wallpaper generator";
          mainProgram = "wallpaper-generator";
        };
      };
    in {
      inherit wallpaper-generator;
      default = wallpaper-generator;
    });
  };
}
