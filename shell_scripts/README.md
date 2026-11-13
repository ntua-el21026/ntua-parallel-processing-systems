# Historical lab-access helpers

These four Bash scripts were used to transfer work between a WSL workstation, Orion, and Scirouter for the NTUA Parallel Processing Systems course. They preserve the original **Michail Athanasios Peppas / parlab05** workflow (2025), with site-specific accounts and paths. They are not required for local source inspection or compilation.

| Script | Behavior | Required local configuration |
| --- | --- | --- |
| [mount_orion.sh](mount_orion.sh) | Creates a mount point and uses SSHFS to mount the Orion home directory | Original `REMOTE`, `KEY_PATH`, and `MOUNT_POINT` values must match your authorized account and workstation |
| [unmount_orion.sh](unmount_orion.sh) | Unmounts with `fusermount -u`, then attempts `rmdir` on the empty mount directory | Uses the same fixed mount point as the mount script |
| [push_to_scirouter.sh](push_to_scirouter.sh) | Copies a source directory's contents, including dotfiles, to Scirouter | SSH alias `scirouter`, SSH/SCP access, and destination permissions |
| [push_to_orion.sh](push_to_orion.sh) | Copies a source directory's contents, including dotfiles, to Orion | SSH alias `orion`, SSH/SCP access, and destination permissions |

The mount scripts retain `$HOME/Parallel_Processing_Systems/orion_home`, the original lab host/account, and a WSL key-file path. `Parallel_Processing_Systems` here is a historical runtime path, not the current repository name. Changing the Git clone directory does not update these script constants. Use a reviewed local copy with appropriate paths rather than assuming the scripts are portable.

After configuring a transfer helper for your own authorized environment, its interface is:

```bash
bash shell_scripts/push_to_scirouter.sh <source_dir> [destination_name]
bash shell_scripts/push_to_orion.sh <source_dir> [destination_name]
```

Both transfer scripts create the destination directory over SSH and use `scp -Crp` to preserve permissions/timestamps and request compression. They copy into an existing destination and may overwrite same-named files; they are not transactional synchronization tools. The optional destination name defaults to the source basename. The mount helper requires SSHFS and a suitable FUSE setup; key authentication must be configured separately.
