# Agent

The Agent is a conversational assistant designed to help team members in organizations establish a shared information context and work more efficiently together. The agent is built using Python and langchain.

## Setup and Installation

1. Install [nix](https://nixos.org/download.html#nix-install-macos)

2. To test installation, run `echo $PATH` and ensure `{...}/.nix-profile/bin` is the first element; if not, try `export PATH=$HOME/.nix-profile/bin:$PATH`

3. Make sure you have the nix-pkgs channel set, ie.

```
nix-channel --add https://nixos.org/channels/nixpkgs-unstable
nix-channel --update
```

## Running the agent with zulip

1. Run `nix-shell` from the directory where `shell.nix` exists (ie the root of this repo), and you should be dropped into a new shell environment with the necessary dependencies installed.

2. Run `poetry install` to install the python dependencies from pyproject.toml. This will create a virtual environment and install the necessary python dependencies within.

3. Run `poetry shell`. This will run the virtual environment that was created in the previous step.

4. Set the OPENAI_API_KEY environment variable in your shell.

5. The agent_config.json file is a sample configuration file. Copy it to ~/agent_config.json and set the DATA_DIR variable to the absolute path of the directory of files that you want to input to the agent. This should be a directory containing any notes or thoughts you have about Plurigrid. If you instead want to the agent's index to be constructed from
messages on a discord server, add the relevant discord channel IDs to the `CHANNEL_IDS` variable in agent_config.json. Make sure you set the INDEX_MODE variable to either "discord" or "directory". In order for the channels to be read, you need to set the `DISCORD_TOKEN` environment variable to your discord bot's API key.

6. If running a zulip bot, you will also need a zulip bot API key. You already have a bot created for you, so go to Zulip and navigate to 'Settings' --> 'Personal Settings' --> 'Bots'. Download the zuliprc file. Copy the api key and use it to set the `ZULIP_BOT_KEY` environment variable in your shell. Then, in ~/agent_config.json, set the BOT_EMAIL variable to your bot's email address. Set the SERVER_URL variable to the zulip server url.

7. If running a discord bot, you will need to set the `DISCORD_TOKEN` environment variable to your bot's API key.

8. Run your agent and indicate which bot type you want: `python3 agent/agents/digital_twin.py --bot-type {discord, zulip}`. Make sure you run this command from the root of the repo.

9. If all has gone well, you can now interact with your bot by tagging it and asking it questions.

## Tips

- To exit the poetry shell, type `exit`
- To exit the nix shell, use `Ctrl + d`
- If you need to reinstantiate your env, do `poetry env list` and then paste the outputted env into `poetry env remove {env-name}`. Then, run `poetry install` and `poetry shell` again to instantiate a new env.

## Organizational Loops

In its current form, the Agent facilitates a daily "gm --> gn" loop for team members. When a team member says "gm" to the agent, it prompts each team member to share their intentions for the day, starting with the person who initiated the conversation. The agent records each person's response. When a team member says "gn" to the agent, it prompts each team member to share what they accomplished that day, starting with the person who initiated the conversation. The agent records each person's response and can output a work dependency graph based on the data collected.

The agent can also be fed an index based on a user's personal markdown files, and the agent can then be used to query this knowledge.  

## Microworlds

The Agent will be used in the future to generate microworlds, which represent particular simulation contexts for various domains involving a set of coordination strategies, agents, and an environment. Human experts (or automated assurance systems) will validate the outputs of the agents and select which subset of microworlds they have generated are actually valid or safe. The output of this validation process will be used to re-train and fine-tune the agents, making them more effective at what they do.

## Appendix

### Reproducibility

`nix` and `poetry` allow for [packaging for serverless execution](https://github.com/bananaml/serverless-template) with reliable system, package, and other application dependencies like Secrets correctly derived for individual `agent` runtime environment.
