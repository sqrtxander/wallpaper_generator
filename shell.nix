{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  packages = [
    pkgs.ty
    (pkgs.python313.withPackages (p:
      with p; [
        numpy
        pillow
        scipy
        ruff
      ]))
  ];
}
