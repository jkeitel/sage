- David Roe, Frej Drejhammar, Julian Rueth, Martin Raum, Nicolas M. Thiery, R.
import re
GIT_BRANCH_REGEX = re.compile(r'^(?!.*/\.)(?!.*\.\.)(?!/)(?!.*//)(?!.*@\{)(?!.*\\)[^\040\177 ~^:?*[]+(?<!\.lock)(?<!/)(?<!\.)$') # http://stackoverflow.com/questions/12093748/how-do-i-check-for-valid-git-branch-names
# The first line should contain a short summary of your changes, the following
# lines should contain a more detailed description.
# Lines starting with '#' are ignored.
class SageDev(object):
    - ``config`` -- a :class:`config.Config` or ``None`` (default: ``None``),
      the configuration of this object; the defaults uses the configuration
      stored in ``DOT_SAGE/devrc``.
    - ``UI`` -- a :class:`user_interface.UserInterface` or ``None`` (default:


                self._UI.show("The developer scripts used to store some of their data in `{0}`. This file has now moved to `{1}`. I moved `{0}` to `{1}`. This might cause trouble if this is a fresh clone of the repository in which you never used the developer scripts before. In that case you should manually delete `{1}` now.".format(old_file, new_file))
        move_legacy_saving_dict('ticketfile', self.config['sagedev'].get('ticketfile', os.path.join(DOT_SAGE, 'branch_to_ticket')), ticket_file)
        move_legacy_saving_dict('branchfile', self.config['sagedev'].get('branchfile', os.path.join(DOT_SAGE, 'ticket_to_branch')), branch_file)
        move_legacy_saving_dict('dependenciesfile', self.config['sagedev'].get('dependenciesfile', os.path.join(DOT_SAGE, 'dependencies')), dependencies_file)
        move_legacy_saving_dict('remotebranchesfile', self.config['sagedev'].get('remotebranchesfile', os.path.join(DOT_SAGE, 'remote_branches')), remote_branches_file)

            import tempfile
            self._tmp_dir = tempfile.mkdtemp()


            self._UI.info("Created ticket #{0}.".format(ticket))
            self._UI.info("Ticket creation aborted.")

        self._UI.info("To start work on ticket #{0}, create a branch for this ticket and check it out with `{1}`.".format(ticket, self._format_command("checkout", ticket=ticket)))
       Checking out a branch::

            ValueError: `1` is not a valid ticket name or ticket does not exist on trac.
            The branch `u/bob/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            Ticket #1 refers to the non-existant local branch `ticket/1`. If you have not manually interacted with git, then this is a bug in sagedev. Removing the association from ticket #1 to branch `ticket/1`.
            This happened while executing `git -c user.email=doc@test.test -c user.name=alice checkout ticket/1`.
            sage: open("tracked","w").close()
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] d
            ValueError: `1000` is not a valid ticket name or ticket does not exist on trac.
            ValueError: Branch field is not set for ticket #5 on trac.
            sage: UI.append("n")
            Your repository is in an unclean state. It seems you are in the middle of a merge of some sort. To complete this command you have to reset your repository to a clean state. Do you want me to reset your repository? (This will discard many changes which are not commited.) [yes/No] n
            Could not check out branch `ticket/8` because your working directory is not in a clean state.
            sage: UI.append("keep")
            sage: dev.checkout(ticket=9) # the new branch is based on master which is not the same commit as the current branch ticket/7 - so it is not a valid option to 'keep' changes
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? Your command can only be completed if you discard or stash your changes. [discard/Keep/stash] keep
            Could not check out branch `ticket/9` because your working directory is not clean.
            sage: dev.checkout(ticket=10, base='ticket/7') # now we can keep changes because the base is the same commit as the current branch
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] keep

            self._UI.info("The branch for ticket #{0} is now `{1}`.".format(ticket, branch))
            self._UI.info("Now checking out branch `{0}`.".format(branch))
                self._UI.info("Checking out branch `{0}`.".format(branch))
            raise SageDevValueError("currently on no ticket, `base` must not be None")
                    self._UI.info("The branch field on ticket #{0} is not set. Creating a new branch `{1}` off the master branch `{2}`.".format(ticket, branch, MASTER_BRANCH))
                        self._UI.error("The branch field on ticket #{0} is set to `{1}`. However, the branch `{1}` does not exist. Please set the field on trac to a field value.".format(ticket, remote_branch))
                        self._UI.info("Created a new branch `{0}` based on `{1}`.".format(branch, remote_branch))
                        self._UI.error("Could not check out ticket #{0} because the remote branch `{1}` for that ticket could not be pulled.".format(ticket, remote_branch))
                    if not self._UI.confirm("Creating a new branch for #{0} based on `{1}`. The trac ticket for #{0} already refers to the branch `{2}`. As you are creating a new branch for that ticket, it seems that you want to ignore the work that has already been done on `{2}` and start afresh. Is this what you want?".format(ticket, base, remote_branch), default=False):
                        self._UI.info("To work on a fresh copy of `{0}`, use `{1}`.".format(remote_branch, command))
                self._UI.info("Creating a new branch for #{0} based on `{1}`.".format(ticket, base))
                self._UI.info("Deleting local branch `{0}`.")
            self._UI.info("Locally recording dependency on {0} for #{1}.".format(", ".join(["#"+str(dep) for dep in dependencies]), ticket))
        self._set_remote_branch_for_branch(branch, self._remote_branch_for_ticket(ticket)) # set the remote branch for branch to the default u/username/ticket/12345
        self._UI.info("Checking out to newly created branch `{0}`.".format(branch))
    def checkout_branch(self, branch):
        - ``branch`` - a string, the name of a local branch
       Checking out a branch::
            ValueError: Branch `branch3` does not exist locally.
            sage: open("untracked","w").close()
            sage: open("tracked","w").close()
            sage: UI.append("keep")
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? Your command can only be completed if you discard or stash your changes. [discard/Keep/stash] keep
            Could not check out branch `branch1` because your working directory is not clean.
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? Your command can only be completed if you discard or stash your changes. [discard/Keep/stash] s
            Your changes have been recorded on a new branch `stash/1`.

        And unstash the changes later::
            sage: dev.unstash()
            stash/1
            sage: UI.append("n")
            sage: dev.unstash('stash/1')
            The changes recorded in `stash/1` have been restored in your working directory.  Would you like to delete the branch they were stashed in? [Yes/no] n
            sage: UI.append("d")
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? Your command can only be completed if you discard or stash your changes. [discard/Keep/stash] d
            sage: UI.append('n')
            Your repository is in an unclean state. It seems you are in the middle of a merge of some sort. To complete this command you have to reset your repository to a clean state. Do you want me to reset your repository? (This will discard many changes which are not commited.) [yes/No] n
            Could not check out branch `merge_branch` because your working directory is not in a clean state.
            sage: dev.git.reset_to_clean_state()
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? Your command can only be completed if you discard or stash your changes. [discard/Keep/stash] discard
            This happened while executing `git -c user.email=doc@test.test -c user.name=doctest checkout branch2`.
            error: The following untracked working tree files would be overwritten by checkout:

            self.reset_to_clean_state()
            self._UI.error("Could not check out branch `{0}` because your working directory is not in a clean state.".format(branch))
            self._UI.info("To checkout `{0}`, use `{1}`.".format(branch, self._format_command("checkout",branch=branch)))
            self.reset_to_clean_working_directory(cancel_unless_clean = (current_commit != target_commit))
            self._UI.error("Could not check out branch `{0}` because your working directory is not clean.".format(branch))
            # this leaves locally modified files intact (we only allow this to happen if current_commit == target_commit
            ValueError: Branch field is not set for ticket #1 on trac.
            The branch `u/alice/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            Merging the remote branch `u/alice/ticket/1` into the local branch `ticket/1`.
            The branch `u/bob/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/alice/ticket/1` to `u/bob/ticket/1`. Is this what you want? [Yes/no] y
            Merging the remote branch `u/bob/ticket/1` into the local branch `ticket/1`.
            I will now push the following new commits to the remote branch `u/bob/ticket/1`:
            ...: bob: added alices_file
            Is this what you want? [Yes/no] y
            Merging the remote branch `u/bob/ticket/1` into the local branch `ticket/1`.
            There was an error during the merge. Most probably there were conflicts when merging. The following should make it clear which files are affected:
            Please fix conflicts in the affected files (in a different terminal) and type 'resolved'. Or type 'abort' to abort the merge. [resolved/abort] abort
            Merging the remote branch `u/bob/ticket/1` into the local branch `ticket/1`.
            I will now push the following new commits to the remote branch `u/bob/ticket/1`:
            ...: bob: added bobs_other_file
            Is this what you want? [Yes/no] y
            Merging the remote branch `u/bob/ticket/1` into the local branch `ticket/1`.
            There was an error during the merge. Most probably there were conflicts when merging. The following should make it clear which files are affected:
                bobs_other_file
            Aborting
            Please fix conflicts in the affected files (in a different terminal) and type 'resolved'. Or type 'abort' to abort the merge. [resolved/abort] abort
            raise SageDevValueError("No `ticket_or_remote_branch` specified to pull.")
        self._UI.info("Fetching remote branch `{0}` into `{1}`.".format(remote_branch, branch))
                e.explain = "Fetching `{0}` into `{1}` failed.".format(remote_branch, branch)
                    e.explain += " Most probably this happened because the fetch did not resolve as a fast-forward, i.e., there were conflicting changes."
                    e.advice = "You can try to use `{2}` to checkout `{1}` and then use `{3}` to resolve these conflicts manually.".format(remote_branch, branch, self._format_command("checkout",branch=branch), self._format_command("merge",remote_branch,pull=True))
                    e.explain += "We did not expect this case to occur.  If you can explain your context in sage.dev.sagedev it might be useful to others."
                    pass
        - :meth:`push` -- Push changes to the remote server.  This
          is the next step once you've committed some changes.
        - :meth:`diff` -- Show changes that will be committed.
            sage: dev.git.super_silent.checkout('-b','branch1')
            sage: dev._UI.extend(["added tracked","y","y","y"])
             tracked
            Do you want to add any of these files in this commit? [yes/No] y
            Do you want to add `tracked`? [yes/No] y
            Do you want to commit your changes to branch `branch1`? I will prompt you for a commit message if you do. [Yes/no] y
            sage: with open("tracked","w") as F: F.write("foo")
            sage: dev._UI.extend(["modified tracked","y"])
            sage: dev.commit()
            Do you want to commit your changes to branch `branch1`? I will prompt you for a commit message if you do. [Yes/no] y

            self._UI.info("Use `{0}` to checkout a branch.".format(self._format_command("checkout")))
            self._UI.info("Committing pending changes to branch `{0}`.".format(branch))
                    if self._UI.confirm("The following files in your working directory are not tracked by git:\n{0}\nDo you want to add any of these files in this commit?".format("\n".join([" "+fname for fname in untracked_files])), default=False):
                            if self._UI.confirm("Do you want to add `{0}`?".format(file), default=False):
                if not self._UI.confirm("Do you want to commit your changes to branch `{0}`?{1}".format(branch, " I will prompt you for a commit message if you do." if message is None else ""), default=True):
                    self._UI.info("If you want to commit to a different branch/ticket, run `{0}` first.".format(self._format_command("checkout")))
                    raise OperationCancelledError("user does not want to create a commit")

                    from tempfile import NamedTemporaryFile
                    commit_message = NamedTemporaryFile()
                    commit_message.write(COMMIT_GUIDE)
                    commit_message.flush()

                    self._UI.edit(commit_message.name)

                    message = "\n".join([line for line in open(commit_message.name).read().splitlines() if not line.startswith("#")]).strip()

                self._UI.info("A commit has been created.")

                self._UI.info("Not creating a commit.")
        - :meth:`push` -- To push changes after setting the remote branch

                self._UI.error("`branch` must not be None because you are in detached HEAD state.")
                self._UI.info("Checkout a branch with `{0}` or specify branch explicitly.".format(self._format_command('checkout')))
                self._UI.error("no local branch for ticket #{0} found. Cannot set remote branch for that ticket.".format(ticket))
            self._UI.warning("The remote branch `{0}` is not in your user scope. You might not have permission to push to that branch. Did you mean to set the remote branch to `u/{1}/{0}`?".format(remote_branch, self.trac._username))
        - :meth:`commit` -- Save changes to the local repository.
        - :meth:`pull` -- Update a ticket with changes from the remote
          repository.
        TESTS::
            ValueError: `1` is not a valid ticket name or ticket does not exist on trac.
            The branch `u/alice/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            The branch `u/bob/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/alice/ticket/1` to `u/bob/ticket/1`. Is this what you want? [Yes/no] y
            Merging the remote branch `u/bob/ticket/1` into the local branch `ticket/1`.
            I will now push the following new commits to the remote branch `u/alice/ticket/1`:
            ...: alice: modified tracked
            ...: bob: modified tracked
            Is this what you want? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/bob/ticket/1` to `u/alice/ticket/1`. Is this what you want? [Yes/no] y
            I will now push the following new commits to the remote branch `u/bob/ticket/1`:
            ...: bob: added tracked2
            Is this what you want? [Yes/no] y
            Not setting the branch field for ticket #1 to `u/bob/ticket/1` because `u/bob/ticket/1` and the current value of the branch field `u/alice/ticket/1` have diverged.
            Merging the remote branch `u/alice/ticket/1` into the local branch `ticket/1`.
            I will now push the following new commits to the remote branch `u/bob/ticket/1`:
            ...: Merge branch 'u/alice/ticket/1' of ... into ticket/1
            ...: alice: modified tracked
            Is this what you want? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/alice/ticket/1` to `u/bob/ticket/1`. Is this what you want? [Yes/no] y
            ValueError: `2` is not a valid ticket name or ticket does not exist on trac.
            You are trying to push the branch `ticket/1` to `u/bob/ticket/2` for ticket #2. However, your local branch for ticket #2 seems to be `ticket/2`. Do you really want to proceed? [yes/No] y
            The branch `u/bob/ticket/2` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            The branch `u/bob/branch1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/bob/ticket/1` to `u/bob/branch1`. Is this what you want? [Yes/no] y
            Merging the remote branch `u/bob/ticket/2` into the local branch `ticket/1`.
            sage: bob._UI.append("y")
            I will now change the branch field of ticket #1 from its current value `u/bob/branch1` to `u/bob/ticket/1`. Is this what you want? [Yes/no] y
            Uploading your dependencies for ticket #1: `` => `#2`
            sage: bob._UI.append("keep")
            According to trac, ticket #1 depends on #2. Your local branch depends on no tickets. Do you want to upload your dependencies to trac? Or do you want to download the dependencies from trac to your local branch? Or do you want to keep your local dependencies and the dependencies on trac in its current state? [upload/download/keep] keep
            sage: bob._UI.append("download")
            According to trac, ticket #1 depends on #2. Your local branch depends on no tickets. Do you want to upload your dependencies to trac? Or do you want to download the dependencies from trac to your local branch? Or do you want to keep your local dependencies and the dependencies on trac in its current state? [upload/download/keep] download
            sage: bob.push()

                    raise SageDevValueError("remote_branch must be specified since #{0} has no remote branch set.".format(ticket))
                    raise SageDevValueError("remote_branch must be specified since the current branch has no remote branch set.")

        user_confirmation = force
                if user_confirmation or self._UI.confirm("You are trying to push the branch `{0}` to `{1}` for ticket #{2}. However, your local branch for ticket #{2} seems to be `{3}`. Do you really want to proceed?".format(branch, remote_branch, ticket, self._local_branch_for_ticket(ticket)), default=False):
                    self._UI.info("To permanently set the branch associated to ticket #{0} to `{1}`, use `{2}`.".format(ticket, branch, self._format_command("checkout",ticket=ticket,branch=branch)))
                    user_confirmation = True
                if user_confirmation or self._UI.confirm("You are trying to push the branch `{0}` to `{1}` for ticket #{2}. However, that branch is associated to ticket #{3}. Do you really want to proceed?".format(branch, remote_branch, ticket, self._ticket_for_local_branch(branch))):
                    self._UI.info("To permanently set the branch associated to ticket #{0} to `{1}`, use `{2}`. To create a new branch from `{1}` for #{0}, use `{3}` and `{4}`.".format(ticket, branch, self._format_command("checkout",ticket=ticket,branch=branch), self._format_command("checkout",ticket=ticket), self._format_command("merge", branch=branch)))
                    user_confirmation = True

        self._UI.info("Pushing your changes in `{0}` to `{1}`.".format(branch, remote_branch))
                if not self._UI.confirm("The branch `{0}` does not exist on the remote server yet. Do you want to create the branch?".format(remote_branch), default=True):
                    self._UI.error("Not pushing your changes because they would discard some of the commits on the remote branch `{0}`.".format(remote_branch))
                    self._UI.info("If this is really what you want, use `{0}` to push your changes.".format(self._format_command("push",ticket=ticket,remote_branch=remote_branch,force=True)))
            if remote_branch_exists and not force and self.git.commit_for_branch(branch) == self.git.commit_for_ref('FETCH_HEAD'):
                self._UI.info("Not pushing your changes because the remote branch `{0}` is idential to your local branch `{1}`. Did you forget to commit your changes with `{2}`?".format(remote_branch, branch, self._format_command("commit")))
                            if not self._UI.confirm("I will now push the following new commits to the remote branch `{0}`:\n{1}Is this what you want?".format(remote_branch, commits), default=True):
                    self.git.super_silent.push(self.git._repository, "{0}:{1}".format(branch, remote_branch), force=force)

            self._UI.info("Your changes in `{0}` have been pushed to `{1}`.".format(branch, remote_branch))

            self._UI.info("Did not push any changes.")

                self._UI.info("Not setting the branch field for ticket #{0} because it already points to your branch `{1}`.".format(ticket, remote_branch))
                self._UI.info("Setting the branch field of ticket #{0} to `{1}`.".format(ticket, remote_branch))

                        self._UI.error("Not setting the branch field for ticket #{0} to `{1}` because `{1}` and the current value of the branch field `{2}` have diverged.".format(ticket, remote_branch, current_remote_branch))
                        self._UI.info("If you really want to overwrite the branch field use `{0}`. Otherwise, you need to merge in the changes introduced by `{2}` by using `{1}`.".format(self._format_command("push",ticket=ticket,remote_branch=remote_branch,force=True), self._format_command("download", ticket=ticket), current_remote_branch))
                    if not self._UI.confirm("I will now change the branch field of ticket #{0} from its current value `{1}` to `{2}`. Is this what you want?".format(ticket, current_remote_branch, remote_branch), default=True):
                    sel = self._UI.select("According to trac, ticket #{0} depends on {1}. Your local branch depends on {2}. Do you want to upload your dependencies to trac? Or do you want to download the dependencies from trac to your local branch? Or do you want to keep your local dependencies and the dependencies on trac in its current state?".format(ticket,old_dependencies,new_dependencies or "no tickets"),options=("upload","download","keep"))
                        self._UI.info("Setting dependencies for #{0} to {1}.".format(ticket, old_dependencies))
                self._UI.info("Not uploading your dependencies for ticket #{0} because the dependencies on trac are already up-to-date.".format(ticket))
                self._UI.show("Uploading your dependencies for ticket #{0}: `{1}` => `{2}`".format(ticket, old_dependencies, new_dependencies))

    def reset_to_clean_state(self, cancel_unless_clean=True):
        - ``cancel_unless_clean`` -- a boolean (default: ``True``), whether to
          raise an :class:`user_interface_error.OperationCancelledError` if the
            sage: UI.append("n")
            Your repository is in an unclean state. It seems you are in the middle of a merge of some sort. To complete this command you have to reset your repository to a clean state. Do you want me to reset your repository? (This will discard many changes which are not commited.) [yes/No] n
            sage: UI.append("y")
            Your repository is in an unclean state. It seems you are in the middle of a merge of some sort. To complete this command you have to reset your repository to a clean state. Do you want me to reset your repository? (This will discard many changes which are not commited.) [yes/No] y

        if not self._UI.confirm("Your repository is in an unclean state. It seems you are in the middle of a merge of some sort. {0}Do you want me to reset your repository? (This will discard many changes which are not commited.)".format("To complete this command you have to reset your repository to a clean state. " if cancel_unless_clean else ""), default=False):
            if not cancel_unless_clean:
        self.git.reset_to_clean_state()

    def reset_to_clean_working_directory(self, cancel_unless_clean=True):
        Drop any uncommitted changes in the working directory.
        - ``cancel_unless_clean`` -- a boolean (default: ``True``), whether to
          raise an :class:`user_interface_error.OperationCancelledError` if the
            sage: dev.reset_to_clean_working_directory()
            sage: dev.reset_to_clean_working_directory()
            sage: dev.reset_to_clean_working_directory()
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? Your command can only be completed if you discard or stash your changes. [discard/Keep/stash] discard
            sage: dev.reset_to_clean_working_directory()
            sage: UI.append("keep")
            sage: dev.reset_to_clean_working_directory()
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? Your command can only be completed if you discard or stash your changes. [discard/Keep/stash] keep
            sage: dev.reset_to_clean_working_directory()
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? Your command can only be completed if you discard or stash your changes. [discard/Keep/stash] stash
            Your changes have been recorded on a new branch `stash/1`.
            sage: dev.reset_to_clean_working_directory()

            self.reset_to_clean_state(cancel_unless_clean)
        files = "\n".join([line[2:] for line in self.git.status(porcelain=True).splitlines() if not line.startswith('?')])
        sel = self._UI.select("The following files in your working directory contain uncommitted changes:\n{0}\nDo you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later?{1}".format(files, " Your command can only be completed if you discard or stash your changes." if cancel_unless_clean else ""), options=('discard','keep','stash'), default=1)
            self.git.reset_to_clean_working_directory()
        elif sel == 'keep':
            if cancel_unless_clean:
            from git_error import DetachedHeadError
            try:
                current_branch = self.git.current_branch()
            except DetachedHeadError:
                current_branch = None
                current_commit = self.git.current_commit()

            branch = self._new_local_branch_for_stash()
            try:
                try:
                    self.git.super_silent.stash()
                    try:
                        self._UI.info("Creating a new branch `{0}` which contains your stashed changes.".format(branch))
                        self.git.super_silent.stash('branch',branch,'stash@{0}')
                        self._UI.info("Committing your changes to `{0}`.".format(branch))
                        self.git.super_silent.commit('-a',message="Changes stashed by reset_to_clean_working_directory()")
                    except:
                        self.git.super_silent.stash('drop')
                        raise
                except:
                    if self._is_local_branch_name(branch, exists=True):
                        self.git.super_silent.branch("-D",branch)
                    raise
            finally:
                self.git.super_silent.checkout(current_branch or current_commit)

            self._UI.show("Your changes have been recorded on a new branch `{0}`.".format(branch))
            self._UI.info("To recover your changes later use `{1}`.".format(branch, self._format_command("unstash",branch=branch)))
            raise NotImplementedError

    def unstash(self, branch=None, show_diff=False):
        r"""
        Unstash the changes recorded in ``branch``.

        INPUT:

        - ``branch`` -- the name of a local branch or ``None`` (default:
          ``None``), if ``None`` list all stashes.
        - ``show_diff`` -- if ``True``, shows the diff stored in the
          stash rather than applying it.

        TESTS:

        Set up a single user for doctesting::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

        Create some stashes::

            sage: dev.unstash()
            (no stashes)
            sage: with open("tracked", "w") as f: f.write("foo")
            sage: dev.git.silent.add("tracked")
            sage: UI.append("s")
            sage: dev.reset_to_clean_working_directory()
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? Your command can only be completed if you discard or stash your changes. [discard/Keep/stash] s
            Your changes have been recorded on a new branch `stash/1`.
            sage: with open("tracked", "w") as f: f.write("boo")
            sage: dev.git.silent.add("tracked")
            sage: UI.append("s")
            sage: dev.reset_to_clean_working_directory()
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? Your command can only be completed if you discard or stash your changes. [discard/Keep/stash] s
            Your changes have been recorded on a new branch `stash/2`.
            sage: dev.unstash()
            stash/1
            stash/2

        See what's in a stash::

            sage: dev.unstash("stash/1", show_diff=True)
            diff --git a/tracked b/tracked
            new file mode 100644
            index 0000000...
            --- /dev/null
            +++ b/tracked
            @@ -0,0 +1 @@
            +foo
            \ No newline at end of file

        Unstash a change::

            sage: UI.append("y")
            sage: dev.unstash("stash/1")
            The changes recorded in `stash/1` have been restored in your working directory.  Would you like to delete the branch they were stashed in? [Yes/no] y

        Unstash something that is not a stash::

            sage: dev.unstash("HEAD")
            ValueError: `HEAD` is not a valid name for a stash.

        Unstash a conflicting change::

            sage: dev.unstash("stash/2")
            The changes recorded in `stash/2` do not apply cleanly to your working directory.

        """
        if branch is None:
            stashes = [stash for stash in self.git.local_branches() if self._is_stash_name(stash)]
            stashes.sort()
            stashes = "\n".join(stashes)
            stashes = stashes or "(no stashes)"
            self._UI.info("Use `{0}` to apply the changes recorded in the stash to your working directory, or `{1}` to see the changes recorded in the stash, where `name` is one of the following.".format(self._format_command("unstash",branch="name"), self._format_command("unstash",branch="name",show_diff=True), stashes))
            self._UI.show(stashes)
            return
        elif show_diff:
            self.git.echo.diff(branch + '^..' + branch)
            return

        self._check_stash_name(branch, exists=True)

        self.reset_to_clean_state()

        try:
            try:
                self.git.super_silent.cherry_pick(branch, no_commit=True)
            finally:
                self.git.super_silent.reset()
        except GitError as e:
            self._UI.error("The changes recorded in `{0}` do not apply cleanly to your working directory.".format(branch))
            self._UI.info("Some of your files now have conflict markers.  You should resolve the changes manually or use `{0}` to reset to the last commit, but be aware that this command will undo any uncommitted changes".format(self._format_command("reset_to_clean_working_directory")))
            raise OperationCancelledError("unstash failed")

        if self._UI.confirm("The changes recorded in `{0}` have been restored in your working directory.  Would you like to delete the branch they were stashed in?".format(branch), True):
            self.git.branch(branch, D=True)

        """
        - ``ticket`` -- an integer or string identifying a ticket or ``None``
        (default: ``None``), the number of the ticket to edit.  If ``None``,
        edit the :meth:`_current_ticket`.
            The branch `u/doctest/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
        self._UI.info("Ticket #%s marked as needing review"%ticket)
        """
        - ``ticket`` -- an integer or string identifying a ticket or ``None``
        (default: ``None``), the number of the ticket to edit.  If ``None``,
        edit the :meth:`_current_ticket`.
            The branch `u/alice/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
        self._UI.info("Ticket #%s marked as needing work"%ticket)
        """
        - ``ticket`` -- an integer or string identifying a ticket or ``None``
        (default: ``None``), the number of the ticket to edit.  If ``None``,
        edit the :meth:`_current_ticket`.
            The branch `u/alice/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
        self._UI.info("Ticket #%s marked as needing info"%ticket)
        """
        - ``ticket`` -- an integer or string identifying a ticket or ``None``
        (default: ``None``), the number of the ticket to edit.  If ``None``,
        edit the :meth:`_current_ticket`.
            The branch `u/alice/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
        self._UI.info("Ticket #%s reviewed!"%ticket)


            ValueError: ticket must be specified if not currently on a ticket.
            Your branch `ticket/1` has 0 commits.
            The branch `u/doctest/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            Your branch `ticket/1` has 0 commits.
            The trac ticket points to the branch `u/doctest/ticket/1` which has 0 commits. It does not differ from `ticket/1`.
            Your branch `ticket/1` has 1 commits.
            The trac ticket points to the branch `u/doctest/ticket/1` which has 0 commits. `ticket/1` is ahead of `u/doctest/ticket/1` by 1 commits:
            I will now push the following new commits to the remote branch `u/doctest/ticket/1`:
            ...: added tracked
            Is this what you want? [Yes/no] y
            Your branch `ticket/1` has 1 commits.
            The trac ticket points to the branch `u/doctest/ticket/1` which has 1 commits. It does not differ from `ticket/1`.
            Your branch `ticket/1` has 0 commits.
            The trac ticket points to the branch `u/doctest/ticket/1` which has 1 commits. `u/doctest/ticket/1` is ahead of `ticket/1` by 1 commits:
            The branch `u/doctest/branch1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            Your branch `ticket/1` has 2 commits.
            The trac ticket points to the branch `u/doctest/branch1` which has 3 commits. `u/doctest/branch1` is ahead of `ticket/1` by 1 commits:
            Your remote branch `u/doctest/ticket/1` has 1 commits. The branches `u/doctest/ticket/1` and `ticket/1` have diverged.
            `u/doctest/ticket/1` is ahead of `ticket/1` by 1 commits:
            `ticket/1` is ahead of `u/doctest/ticket/1` by 2 commits:

        commits = lambda a, b: list(reversed(self.git.log("{0}..{1}".format(a,b), "--pretty=%an <%ae>: %s").splitlines()))
                return "It does not differ from `{0}`.".format(b)
                return "`{0}` is ahead of `{1}` by {2} commits:\n{3}".format(a,b,len(b_to_a),"\n".join(b_to_a))
                return "`{0}` is ahead of `{1}` by {2} commits:\n{3}".format(b,a,len(a_to_b),"\n".join(a_to_b))
                return "The branches `{0}` and `{1}` have diverged.\n`{0}` is ahead of `{1}` by {2} commits:\n{3}\n`{1}` is ahead of `{0}` by {4} commits:\n{5}".format(a,b,len(b_to_a),"\n".join(b_to_a),len(a_to_b),"\n".join(a_to_b))
            local_summary = "Your branch `{0}` has {1} commits.".format(branch, len(master_to_branch))
                ticket_summary = "The trac ticket points to the branch `{0}` which does not exist."
                ticket_summary = "The trac ticket points to the branch `{0}` which has {1} commits.".format(ticket_branch, len(master_to_ticket))
                        ticket_summary += " The branch can not be compared to your local branch `{0}` because the branches are based on different versions of sage (i.e. the `master` branch)."
            remote_summary = "Your remote branch `{0}` has {1} commits.".format(remote_branch, len(master_to_remote))
                    remote_summary += " The branch can not be compared to your local branch `{0}` because the branches are based on different version of sage (i.e. the `master` branch)."

    def prune_closed_tickets(self):
            sage: dev.local_tickets()
            sage: dev.prune_closed_tickets()
            sage: dev.local_tickets()
            sage: dev.prune_closed_tickets()
            Can not delete `ticket/1` because you are currently on that branch.
            sage: dev.prune_closed_tickets()
            Moved your branch `ticket/1` to `trash/ticket/1`.
            sage: dev.local_tickets()
            sage: dev.prune_closed_tickets()

                    self.abandon(ticket)
    def abandon(self, ticket_or_branch=None):
        - :meth:`prune_closed_tickets` -- abandon tickets that have
          been closed.
        - :meth:`local_tickets` -- list local non-abandoned tickets.
            The branch `u/doctest/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            Can not delete `ticket/1` because you are currently on that branch.
            Moved your branch `ticket/1` to `trash/ticket/1`.
            Creating a new branch for #1 based on `master`. The trac ticket for #1 already refers to the branch `u/doctest/ticket/1`. As you are creating a new branch for that ticket, it seems that you want to ignore the work that has already been done on `u/doctest/ticket/1` and start afresh. Is this what you want? [yes/No] y

                raise SageDevValueError("Can not abandon #{0}. You have no local branch for this ticket.".format(ticket))
                self._UI.error("I will not delete the master branch.")
            if not self.git.is_ancestor_of(branch, MASTER_BRANCH):
                if not self._UI.confirm("I will delete your local branch `{0}`. Is this what you want?".format(branch), default=False):
                    raise OperationCancelledError("user requested")
                    self._UI.error("Can not delete `{0}` because you are currently on that branch.".format(branch))
                    self._UI.info("Use `{0}` to move to a different branch.".format(self._format_command("vanilla")))
            self._UI.show("Moved your branch `{0}` to `{1}`.".format(branch, new_branch))
            self._UI.info("If you want to work on #{0} starting from a fresh copy of the master branch, use `{1}`.".format(ticket, self._format_command("checkout",ticket=ticket,base=MASTER_BRANCH)))
        - :meth:`merge` -- merge into the current branch rather than creating a
          new one
            The branch `u/doctest/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y

            self.reset_to_clean_working_directory()
        self._UI.info("Creating a new branch `{0}`.".format(branch))
                self._UI.info("Merging {2} branch `{0}` into `{1}`.".format(branch_name, branch, local_remote))
            self.git.reset_to_clean_working_directory()
            self._UI.info("Deleted branch `{0}`.".format(branch))
        - :meth:`show_dependencies` -- see the current dependencies.
        - :meth:`GitInterface.merge` -- git's merge command has more options
          and can merge multiple branches at once.
        - :meth:`gather` -- creates a new branch to merge into rather than
          merging into the current branch.
        TESTS::
            Can not merge remote branch for #1. No branch has been set on the trac ticket.
            The branch `u/alice/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            Merging the local branch `ticket/1` into the local branch `ticket/2`.
            Merging the remote branch `u/alice/ticket/1` into the local branch `ticket/2`.
            Merging the local branch `ticket/1` into the local branch `ticket/2`.
            Merging the local branch `ticket/1` into the local branch `ticket/2`.
            ValueError: Branch `ticket/1` does not exist on the remote system.
            The branch `u/bob/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/alice/ticket/1` to `u/bob/ticket/1`. Is this what you want? [Yes/no] y
            Merging the remote branch `u/bob/ticket/1` into the local branch `ticket/2`.
            There was an error during the merge. Most probably there were conflicts when merging. The following should make it clear which files are affected:
            Please fix conflicts in the affected files (in a different terminal) and type 'resolved'. Or type 'abort' to abort the merge. [resolved/abort] abort
            sage: alice._UI.append("resolved")
            Merging the remote branch `u/bob/ticket/1` into the local branch `ticket/2`.
            There was an error during the merge. Most probably there were conflicts when merging. The following should make it clear which files are affected:
            Please fix conflicts in the affected files (in a different terminal) and type 'resolved'. Or type 'abort' to abort the merge. [resolved/abort] resolved
            ValueError: cannot merge a ticket into itself
            self.reset_to_clean_working_directory()
            self._UI.error("You are currently not on any branch. Use `{0}` to checkout a branch.".format(self._format_command("checkout")))
                raise SageDevValueError("`pull` must not be `False` when merging dependencies.")
                raise SageDevValueError("`create_dependency` must not be set when merging dependencies.")
                self._UI.info("Merging dependency #{0}.".format(dependency))
                    self._UI.error("Can not merge remote branch for #{0}. No branch has been set on the trac ticket.".format(ticket))
        elif pull == False or (pull is None and not self._is_remote_branch_name(ticket_or_branch, exists=True)):
                    raise SageDevValueError("`create_dependency` must not be `True` if `ticket_or_branch` is a local branch which is not associated to a ticket.")
                raise SageDevValueError("`create_dependency` must not be `True` if `ticket_or_branch` is a local branch.")
                self._UI.error("Can not merge remote branch `{0}`. It does not exist.".format(remote_branch))
            self._UI.show("Merging the remote branch `{0}` into the local branch `{1}`.".format(remote_branch, current_branch))
            self._UI.show("Merging the local branch `{0}` into the local branch `{1}`.".format(branch, current_branch))
                lines = [line for line in lines if line != "Automatic merge failed; fix conflicts and then commit the result."]
                lines.insert(0, "There was an error during the merge. Most probably there were conflicts when merging. The following should make it clear which files are affected:")
                lines.append("Please fix conflicts in the affected files (in a different terminal) and type 'resolved'. Or type 'abort' to abort the merge.")
                if self._UI.select("\n".join(lines),['resolved','abort']) == 'resolved':
                    self._UI.info("Created a commit from your conflict resolution.")
                    raise OperationCancelledError("user requested")
                self.git.reset_to_clean_working_directory()
                self._UI.info("Not recording dependency on #{0} because #{1} already depends on #{0}.".format(ticket, current_ticket))
                self._UI.show("Added dependency on #{0} to #{1}.".format(ticket, current_ticket))
    def local_tickets(self, include_abandoned=False, cached=True):
        - :meth:`abandon_ticket` -- hide tickets from this method.
        - :meth:`remote_status` -- also show status compared to the
          trac server.
        - :meth:`current_ticket` -- get the current ticket.
            sage: dev.local_tickets()
            sage: dev.local_tickets()

            ret.append(("{0:>7}: {1} {2}".format("#"+str(ticket) if ticket else "", branch, ticket_summary), extra))
        - :meth:`checkout` -- checkout another branch, ready to develop on it.
        - :meth:`pull` -- pull a branch from the server and merge it.

            self.reset_to_clean_working_directory()
                self._UI.error("`{0}` does not exist locally or on the remote server.".format(release))

        - :meth:`commit` -- record changes into the repository.
        - :meth:`local_tickets` -- list local tickets (you may want to commit
          your changes to a branch other than the current one).
            The branch `u/doctest/ticket/1` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            The branch `u/doctest/ticket/2` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            The branch `u/doctest/ticket/3` does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            Merging the remote branch `u/doctest/ticket/1` into the local branch `ticket/3`.
            Merging the remote branch `u/doctest/ticket/2` into the local branch `ticket/3`.
            I will now push the following new commits to the remote branch `u/doctest/ticket/2`:
            ...: added ticket2
            Is this what you want? [Yes/no] y
            I will now push the following new commits to the remote branch `u/doctest/ticket/3`:
            ...: added ticket3
            Is this what you want? [Yes/no] y
            Uploading your dependencies for ticket #3: `` => `#1, #2`