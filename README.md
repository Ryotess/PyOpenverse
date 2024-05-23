

<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Ryotess/PyOpenverse">
    <img src="images/logo.png" alt="Logo" width="512" height="256">
  </a>

<h3 align="center">PyOpenverse-- A Python image/audio search engine base on Openverse</h3>

  <p align="center">
  This is an un-official Python package built with Openverse API, currently we only provide image search api in this beta version. The audio search api will be updated in near future.
    <br />
    <a href="https://github.com/Ryotess/PyOpenverse"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Ryotess/PyOpenverse/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Ryotess/PyOpenverse/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Installation">Installation</a></li>
        <li><a href="#Quick Start">Quick Start</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project
### Built With
[![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Please follow the instructions to install and set up the environment for this project.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Ryotess/PyOpenverse.git
   ```
2. Move to the project
   ```sh
   cd ./PyOpenverse
   ```
3. Build environment
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Quick Start
You can follow the [sample code](https://github.com/Ryotess/ChatGen/blob/main/sample_code.ipynb) to get the sample usage of this package.

<!-- USAGE EXAMPLES -->
## Usage
### Setup
#### How to use this package in your own project?
You can directly copy the folder pyopenverse to your project, here is an example structure design:

```
.
└── your-project/
    ├── your_custom_module/
    │   ├── your_function_1.py
    │   └── your_function_2.py
    ├── PyOpenverse/   <--- Copy & Paste the entire pyopenverse folder here.
    │   ├── auth.py
    │   ├── config.py
    │   └── engine.py
    └── your_main.py
```
#### Set Credential
If you already have a credential of Openverse API, please put your credential into an ```.env``` file with keys ```OPENVERSE_CLIENT_ID``` and ```OPENVERSE_CLIENT_SECRET``` before the following instruction  
### Get Credentials (Optional)
If you don't have a credential of Openverse API, we provide an function for you to get your own API's id and secret key.
```sh
# import packages and create a pyopenverse engine
from pyopenverse.engine import PyOpenverse

openverse = PyOpenverse()
# Register for API access if not already registered
name = "My amazing project"
description = "To access Openverse API"
email = "user@example.com"
openverse.register(name, description, email)
```
This method creates a credential for you(and also create a ```.env``` file in the work directory) and loads it into the engine, thus you can use the engine without insert the credential info again.
### Create a PyOpenverse Engine
```sh
# import packages and create a pyopenverse engine
from pyopenverse.engine import PyOpenverse

openverse = PyOpenverse()
```
The engine loads the creadential from the ```.env``` file you just created.  
If you don't want to use ```.env``` file, you can also insert the creadential by the following code
```sh
openverse = PyOpenverse(client_id="your_client_id", client_secret="your_client_secret")
```


### Search
Now we can use this engine to search images by query (currently only support image search api)
```sh
query = "sunset" # Please change the query into what you wanna search
image_urls = openverse.img_search(query=query) # This will return a list of URL of images
```

### API Info
Moreover, you can also check the information (ex. status, usage,...) of your account by using ```get_info()```
```sh
# Check API information
openverse.get_info()
```



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Apache 2.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

E-Mail: jessforwork2023@gmail.com

Project Link: [https://github.com/Ryotess/ChatGen](https://github.com/Ryotess/PyOpenverse)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- REFERENCES -->
## References

* [Openverse API](https://api.openverse.engineering/v1/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/Ryotess/PyOpenverse.svg?style=for-the-badge
[license-url]: https://github.com/Ryotess/PyOpenverse/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/shaoyanchen
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/pypi/pyversions/numpy
[Python-url]: https://numpy.org/
