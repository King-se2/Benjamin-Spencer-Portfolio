# CS345-Project
### **Topic:**

Our selected topic is the topic of machine learning in classical game theory. More specifically, we would like to use a machine learning model to analyze a given board state in a chess game to determine the best possible next move. Our interest in this topic is driven by an appreciation for the game of chess and the qualities of chess that lend itself to machine learning analysis. There are already extensive databases, theories, and even AI models that have presented a wealth of information on new and old ways to play the game of chess at a competitive level. Furthermore, due to the growth of AI in the field of Chess, we have interesting models to compare ours to once it is trained. Specifically, we are excited to test our trained model against Stockfish, the current leading AI model for chess. Stockfish predicts a range of the best possible moves that can be taken from any given game state and this will allow us to gauge our own model very closely.

### **Data:**
_Link to data: https://database.lichess.org/#puzzles_

Our data contains roughly 3,700,000 entities collected from the popular chess website Lichess. The data contains various chess puzzles and solutions which include features such as the rating of involved players, game openings, game themes, and a current board state in FEN format. The labels of the dataset are the list of best moves required to solve the puzzle in chess UCI format. We are happy with this data set due to the large number of datapoints as we know that larger architectures for neural networks require larger datasets. Furthermore, a puzzle based data point is perfect for training our intended model because it has a confirmed correct outcome. This is difficult to discern from full games because ‘the best move’ is very subjective in game theory.

### Proposed Model:
_Link to referenced model: https://erikbern.com/2014/11/29/deep-learning-for-chess.html_ 

_Link to chess library for python: https://python-chess.readthedocs.io/en/latest/_

The model we will use is a two to three layer neural network. The model will resemble the above link but will include fewer layers to reduce strain on performance during training. We will initially attempt a less wide 3 layer architecture and if this is too resource intensive, we will attempt a shallower architecture. The input vector will include serialized input from the current board state and will perform matrix multiplication in an architecture of dense layers using ReLU. This serialized version of the gamestate will be the most important data transformation in our model as understanding how the model is understanding the chess board is important for understanding our architecture. It is also going to be the most resource intensive part of our input and therefore optimizing it will increase the feasible size of our project. The final hidden layer will condense the output into a single value that indicates which move is the best possible move in that given board state. We intend to work closely with the architecture of our dense layers to achieve the highest accuracy in comparison with Stockfish, while keeping the model’s training resources feasible. 

### Timeline (in weeks):

1. Organizing data and figuring out data serialization.
    * How do we want to encode our game states?
    * What chess evaluation parameters do we want to use (if any)?
    * Do we want to curate our data by rating? Or any other metric?
2. Deciding feature set using a Random Forest model as a baseline.
    * Testing based off decisions made the week before
    * Condensing our scope to an actionable task
3. Constructing the modified neural network model.
    * Developing architectures based of decisions and tests from the last two weeks
    * Implementing our ideas
4. Training and testing.
    * High time cost due to our model and dataset
    * Possibly logistical time for getting access to a computer and or dealing with any bugs we encounter during training
    * Space for refactoring our model and retraining if our testing didn’t given positive results
5. Obtaining graphical analysis of the model.
    * Develop datasets of Stockfish comparisons
    * Visual Representations of the chess moves
    * Graphical Representations of our model
6. Finalizing the model and organizing the final report.
    * Write out a report and include all the visual aids created the week before.

### Team Responsibilities:

Splitting up work in a divide and conquer style doesn’t support communication. Currently, the two of us communicate thoroughly and consistently with each other about the project and have been working together on preparing the project and the proposal. Therefore, the Team Responsibilities we will set are personal rather than work based. If we both follow these three responsibilities, we will complete the project robustly and on time.

* **Communication:** We are both responsible for communicating with the other when we do significant work on the project.
* **Consistency:** We are both responsible for checking in on the project every school day until the end of the semester and preferably doing a small amount of work for it.
* **Reliability:** We are both responsible for keeping an eye on our intended goal for each week until the end of the semester and making sure we’re on track to complete the goal we have set for ourselves.
