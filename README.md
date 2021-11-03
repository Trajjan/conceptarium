![mockuper](https://user-images.githubusercontent.com/20104026/133883441-0faae359-9335-46bf-b10c-27ebb8c274b3.png)

# Conceptarium
A conceptarium (noun. /knsɛptɛriəm/, plural: conceptaria) is a fluid medium for storing, relating, and surfacing thoughts based on a new representation of knowledge. It’s meant to provide a foundation for new tools for thought to build onto, a means to nurture a new tooling ecosystem for knowledge work – a cognitive infrastructure. It embodies a philosophy of knowledge which differs in important ways from the one held by the knowledge graph poster children (e.g. Roam Research, Obsidian, Logseq), and can be deployed today in a self-hosted regime, even on a modest Raspberry Pi.

[Read more...](https://paulbricman.com/thoughtware/conceptarium)

# Installation
The conceptarium is a server app which can be deployed on managed hosting (e.g. DigitalOcean) or in a self-hosted regime (e.g. salvaged desktop, Raspberry Pi 4). The app itself takes up about **1GB RAM** when running.

### Docker

To deploy the conceptarium using Docker, first make sure to have it installed, then simply run the following. 

**Note**: This installation method is not suitable for the Rasberry Pi or other ARM devices, as they need a special version of `pytorch`. To deploy on those, please follow the second installation option (from source).

```
docker run -p 8000:8000 paulbricman/conceptarium 
```

Your conceptarium should be available at `127.0.0.1:8000`. 

### From Source

To set up the conceptarium, clone the repository, and install the requirements using:

```
python3 -m pip install -r requirements.txt
```
**Note**: If you plan to deploy your conceptarium on a Raspberry Pi 4, you'll need a version of `pytorch` compiled for ARM devices, such as [pytorch-rpi](https://github.com/ljk53/pytorch-rpi/blob/master/torch-1.9.0a0%2Bgitd69c22d-cp39-cp39-linux_aarch64.whl).

**Note**: Your system might be missing some prior dependencies. The missing packages show up during installation, and Googling one-liners for installing them is rather straightforward. However, for deploying on Ubuntu, you can also look into the [CI/CD tests](https://github.com/Psionica/conceptarium/blob/main/.github/workflows/pytest.yml) for details on setup.

Once the requirements have been installed, start the web server using in the root of the cloned repository:
```
python3 -m uvicorn main:app --reload
```

Your conceptarium should be available at `127.0.0.1:8000`. 

# Usage

**Note**: If you want to access your conceptarium remotely, you might want to have a look at [ngrok](https://ngrok.com/) and expose local port 8000 to the world via a URL.

Out of the box, the conceptarium exposes endpoints for all relevant interactions which can be accessed through a browser (see mockups below). However, for power users, a host of endpoints are exposed which return JSONs, plain text, image files, and others, rather than web pages. Those can be used to set up the conceptarium as a browser search engine, for creating [AutoKey](https://github.com/autokey/autokey) / [AutoHotKey](https://www.autohotkey.com/) scripts, for setting up [IFTTT](https://ifttt.com/) integrations, and others.

**Please find the complete auto-generated API docs over at `127.0.0.1:8000/docs`.**

The style and color scheme of your conceptarium can be tweaked via `assets/style.css`.

# Further Reading

- [early conceptarium workflows](https://paulbricman.com/reflections/early-conceptarium-workflows)
- [dynamical systems online](https://paulbricman.com/reflections/dynamical-systems-online)
- [ideoponics](https://paulbricman.com/reflections/ideoponics)
- [breaking frames](https://paulbricman.com/reflections/breaking-frames)
- [dixit kernel functions](https://paulbricman.com/reflections/dixit-kernel-functions)

# Screenshots

![mockuper(1)](https://user-images.githubusercontent.com/20104026/133883445-b26de5d2-cd71-4a7f-8c0d-99ae25da2865.png)
![mockuper(2)](https://user-images.githubusercontent.com/20104026/133883515-37e7853f-171e-4760-bf03-a2fc557dc364.png)

# Demos

**Note:** Content listed below uses dummy data and an older design. 

AutoKey "I'm feeling lucky" text-to-image

https://user-images.githubusercontent.com/20104026/134158253-1ff71d90-2f89-40f0-a074-2dd489bd1683.mp4

Browser search shortcut

https://user-images.githubusercontent.com/20104026/134158264-c8b7ecd8-b11c-4b56-9a42-4f4c3a36573f.mp4

Autokey custom text-to-text dialog

https://user-images.githubusercontent.com/20104026/134158276-cadae2cd-6991-41df-a09d-3e9dbc09ba29.mp4

Google Assistant + IFTTT

![eef9e426-06cc-42ff-935b-a74ac64d5991](https://user-images.githubusercontent.com/20104026/134158774-8f820369-d6cc-4e6c-a485-50e29c458061.png)
