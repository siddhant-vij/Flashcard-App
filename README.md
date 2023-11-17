# Flashcard App

A powerful tool for learning and practicing flashcards with boxed-spacing repetitions. It utilizes a CSV database in the backend to store and manage flashcard data. The app also incorporates a queue data structure ensuring that flashcards are presented in the most optimized way for effective learning.

1. [Features](#features)
1. [Installation](#installation)
1. [Contributing](#contributing)
1. [Future Improvements](#future-improvements)
1. [License](#license)

## Features

- **Graphical User Interface (GUI)**: A user-friendly interface that provides an intuitive and interactive experience for users.
- **Flashcard Database**: Utilizes a CSV file to store and manage flashcard data, ensuring efficient retrieval and storage.
- **Queue Data Structure**: Implements a queue data structure to optimize the presentation of flashcards, ensuring an effective learning experience.
- **Boxed-Spacing Repetition Technique**: Utilizes a spaced repetition algorithm to present flashcards at optimal intervals, facilitating long-term memory retention.

## Installation

- Clone the repository: `git clone https://github.com/siddhant-vij/Flashcard-App.git`
- Navigate to the project directory: `cd Flashcard-App`
- Install dependencies: `conda create --name flashcard-app --file requirements.txt`
- Activate the environment: `conda activate flashcard-app`
- Run the application: `python main.py`
- Edit the CSV file: `flashcards.csv`
  - `Front` & `Back` for a topic: Periodic Table
  - start with `1` for all the `Box` entries
  - start with current date for `NextReviewDate`


## Contributing

All contributions to this project are welcome. If you have suggestions or want to contribute to the codebase, please follow the steps below:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## Future Improvements

- **User Progress Tracking**: Implement a feature to track user progress and provide statistics on flashcard performance.
- **Multi-Language Support**: Add support for multiple languages, allowing users to practice flashcards in their preferred language.
- **Audio Pronunciation**: Incorporate audio pronunciation for flashcards, enhancing the learning experience.
- **Social Sharing**: Enable users to share flashcards or their progress on social media platforms.
- **Customizable Flashcard Design**: Allow users to customize the design and layout of their flashcards.
- **Cross-Platform Compatibility**: Ensure the application works seamlessly across different operating systems and devices.


## License

Distributed under the MIT License. See [LICENSE](https://github.com/siddhant-vij/Flashcard-App/blob/main/LICENSE) for more information.
