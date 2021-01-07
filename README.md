# A Python self-hosted GitHub Runner for the Raspberry Pi

small edit

![Python application on self-hosted Raspberry Pi](https://github.com/dogweather/raspberry-pi-python-github-runner/workflows/Python%20application%20on%20self-hosted/badge.svg)


Raspberry Pi's can be used as low-configuration [self-hosted GitHub Runners](https://docs.github.com/en/free-pro-team@latest/actions/hosting-your-own-runners/about-self-hosted-runners). They can do CI builds and tests, and also run [periodic jobs using cron syntax](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions#onschedule):

```bash
pi@pi1 ~/actions-runner> ./run.sh

√ Connected to GitHub

2020-10-06 23:24:36Z: Listening for Jobs
```

This repo solves a problem: GitHub's default Python setup installs
X86 binaries and doesn't work on ARM (Raspberry Pi). So, in the 
process of setting up a new Python app, I extracted this configuration.

Here's a typical [Raspberry Pi runner log](https://github.com/dogweather/raspberry-pi-python-github-runner/runs/1212774604?check_suite_focus=true)
for this repo. Check out how much detail you get vs. running a simple cron job!

This repo is a minimal Python template application which runs several workflows:

* [One - the whole point of this repo](https://github.com/dogweather/raspberry-pi-python-github-runner/blob/main/.github/workflows/python-test.yml) which runs on a self-hosted Raspberry Pi
* [Another](https://github.com/dogweather/raspberry-pi-python-github-runner/blob/main/.github/workflows/python-test-in-cloud.yml) which runs on GitHub's cloud servers
* [Another simple one](https://github.com/dogweather/raspberry-pi-python-github-runner/blob/main/.github/workflows/hello-world.yml), a Hello World shell script which also runs self-hosted

It's also still compatible with MacOS and GitHub's cloud servers.

## How to run this yourself

1. Fork this repo
2. In your new repo's **Settings/Actions**, click **Add runner** and add your Raspberry Pi as a Linux / ARM runner. [GitHub's Docs for this](https://docs.github.com/en/free-pro-team@latest/actions/hosting-your-own-runners/adding-self-hosted-runners)
3. Once the runner is listening for new tasks, make some kind of small commit in your forked repo. You should see tasks sent down to the Raspberry Pi both in the Runner's output and GitHub's Actions tab.

## Compatible Pi's

| Known working | Known not working |
| ------------- | ----------------- |
| Pi 4 Model B 4G RAM w/ Raspberry Pi OS | Pi Zero W |

These were tested on a **Raspberry Pi 4 Model B** with 4G RAM, running Raspberry Pi OS.
I ran two runners on it simultaneously, and there was **tons** of RAM leftover. I suspect it'd
do fine on a Pi with just 1G RAM.

But for some reason, GitHub's runner client won't run on a Pi Zero W (which has 512MB RAM).
The `config` and `run.sh` scripts crash with `Segmentation fault` on startup.
The error seems to be around the `bin/Runner.Listener` invocation. When I try that
command on its own, I get `“bin/Runner.Listener” terminated by signal SIGSEGV (Address boundary error)`.
I suspect that low memory is the issue. RAM is also the only material difference between
the Zero W and 4.
