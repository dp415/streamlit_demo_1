[code boilerplate and project originally outlined by Albers Uzila at https://levelup.gitconnected.com/8-simple-steps-to-build-your-first-streamlit-app-91fe7b3bef9e]

About my versioning and use of Git/Github…
I use a three branch system for development over Git/Github: main, dev, and test. 
1. main branch is the production version with a v#.#.# format. 
2. dev is the development branch, usually created in a local environment with code which reflects that limitation, with a d#.#.# format that is based upon the main version. The program publishes a stable release from dev to main, with dev holding the progressive build of the program. 
3. test is used for debugging, and uses a t#.#.#-#.# format, with the version based upon the dev version that requires further testing/debuggin. The dash in test versions allows for progressive testing versions for specific, static versions of the development program, with the second number in the decimal split being a separate remedy for the issue. This rarely comes up, but has allowed me to test remedies extensively, and have quick access to stable versions, so I will utilize it at some point in most projects.

About this program…
With this program, I am dipslaying basic streamlit operations through a math problem generator. This is a basic Streamlit program, which uses Pandas to convert CSV data (problems are written in LaTeX) into human readable data. This is a template for more complex programs, and I plan to make this code reusable by creating a class structure for page production, and I will be tying the project settings to a YAML file. I may switch from YAML to another format, namely TOML.

To begin the project, I have to transform the original code into something viable, something that actually works and uses contemporary versions of each program/extension. To do that, I fixed some code (mostly directory navigation), generalized some functions, and made a local/remote switch in the program, with local used for development, and remote used for production on a server.

In case you do not know, Streamlit web programs are generally used to present data using Python as a backend. My dev environment has been Jupyter Lab and Notes over a controlled environment managed with Ananconda, with version control over the installable Github program for Windows. I use numpy and the decimal library to manipulate data.
In the near future, I will incorporate every data visualization possible, add more data sources, then manipulate/translate data.
I may switch from Jupyter to Visual Studio Code, where I can use some addons and Github from within the IDE.
