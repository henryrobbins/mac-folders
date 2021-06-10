# mac-folders

This repo contains my custom folder icons for various programs I use. It also
includes a short Python script `update.py` which updates the folder icons on
my machine. Hence, the script makes assumptions about file structure and
folder naming conventions.

## Usage

Using [folderify](https://github.com/lgarron/folderify), a folder icon can be
generated in the native macOS folder style. Here is a simple use case tailored
to this repo. This command generates multiple mac folders from the given icon
at various resolutions.

```folderify icons/git.png```

Additionally, a path to a directory can be given which will update the image
of the folder corresponding to the given directory.

```folderify icons/git.png path/to/folder```

This command is utilized in `update.py`.

## License

Licensed under the [MIT License](https://choosealicense.com/licenses/mit/)