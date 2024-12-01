<a id="readme-top"></a>



<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

[//]: # (  <a href="https://github.com/othneildrew/Best-README-Template">)

[//]: # (    <img src="images/logo.png" alt="Logo" width="80" height="80">)

[//]: # (  </a>)

  <h3 align="center">ComfyUI to CivitAI metadata</h3>

  <p align="center">
    Convert the metadata present on a comfyUI image to those recognized by civitAI ressources
    <br />
    <br />

[//]: # (    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>)
  </p>
</div>



<!-- TABLE OF CONTENTS -->

[//]: # (<details>)

[//]: # (  <summary>Table of Contents</summary>)

[//]: # (  <ol>)

[//]: # (    <li>)

[//]: # (      <a href="#about-the-project">About The Project</a>)

[//]: # (      <ul>)

[//]: # (        <li><a href="#built-with">Built With</a></li>)

[//]: # (      </ul>)

[//]: # (    </li>)

[//]: # (    <li>)

[//]: # (      <a href="#getting-started">Getting Started</a>)

[//]: # (      <ul>)

[//]: # (        <li><a href="#prerequisites">Prerequisites</a></li>)

[//]: # (        <li><a href="#installation">Installation</a></li>)

[//]: # (      </ul>)

[//]: # (    </li>)

[//]: # (    <li><a href="#usage">Usage</a></li>)

[//]: # (    <li><a href="#roadmap">Roadmap</a></li>)

[//]: # (    <li><a href="#contributing">Contributing</a></li>)

[//]: # (    <li><a href="#license">License</a></li>)

[//]: # (    <li><a href="#contact">Contact</a></li>)

[//]: # (    <li><a href="#acknowledgments">Acknowledgments</a></li>)

[//]: # (  </ol>)

[//]: # (</details>)



<!-- ABOUT THE PROJECT -->
## About The Project

![App screenshot][product-screenshot]

This app is an easy-to-use metadata convertor.</br>
It will take your image from ComfyUI and create new metadata that are understand by CivitAI so that you can upload your images, and it automatically detects the Checkpoint, Loras and everything.<br/>
In addition, it keeps the original metadata so that you can still drag and drop your image to ComfyUI to get the workflow.</br>
> **Note**</br>
> This might not work with some custom nodes. It might be fix later if I feel this project has some potential.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![QT][QT]][QT-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Tenko-Gami/Metadata_4_CivitAI.git
   ```   
2. Install the requirement (you can use a venv if you prefer)
   ```sh
   pip install -r requirements.txt
   ```
3. run main.py
   ```sh
   python path\to\Metadata_4_CivitAI\main.py 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### The interface
![App interface][product-interface]
From this interface, you'll have to select the folder 'models' on your comfyUI folder. (as shown in the screenshot).</br>
Then, you'll have to select images to be transformed.</br>
You can see the image using the next and previous button. You can remove any image at any time.</br>

### The execution
To run the program just click the button.</br>
It will create another image next to the one you just selected.</br>
![App create_images][product-create_images]

### The output
You can see the data contained in your images in the output tab.</br>
![App output][product-output]
>**Note**</br>
> It will look better later :)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Make it work
- [x] Add output tab
- [ ] Add error tab
- [ ] Improve graphic style
- [ ] Implement more custom nodes

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Top contributors:

<a href="https://github.com/Tenko-Gami/Metadata_4_CivitAI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Tenko-Gami/Metadata_4_CivitAI" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/Tenko-Gami/Metadata_4_CivitAI](https://github.com/Tenko-Gami/Metadata_4_CivitAI)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Tenko-Gami/Metadata_4_CivitAI.svg?style=for-the-badge
[contributors-url]: https://github.com/Tenko-Gami/Metadata_4_CivitAI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Tenko-Gami/Metadata_4_CivitAI.svg?style=for-the-badge
[forks-url]: https://github.com/Tenko-Gami/Metadata_4_CivitAI/network/members
[stars-shield]: https://img.shields.io/github/stars/Tenko-Gami/Metadata_4_CivitAI.svg?style=for-the-badge
[stars-url]: https://github.com/Tenko-Gami/Metadata_4_CivitAI/stargazers
[issues-shield]: https://img.shields.io/github/issues/Tenko-Gami/Metadata_4_CivitAI.svg?style=for-the-badge
[issues-url]: https://github.com/Tenko-Gami/Metadata_4_CivitAI/issues
[product-screenshot]: images/screenshot.png
[product-interface]: images/interface.png
[product-create_images]: images/create_images.png
[product-output]: images/output.png
[QT]: https://img.shields.io/badge/Qt-41CD52?style=for-the-badge&logo=qt&logoColor=white
[QT-url]: https://wiki.qt.io/Qt_for_Python