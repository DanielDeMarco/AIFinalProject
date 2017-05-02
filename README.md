# AIFinalProject
---------------
##### 1. Which students are on board for your group?

  * Michael Neas 
  * Sean Bridges
  * Angela Onofrio 
  * Cindy Lin 
  * Nick Barber
  * Edward Hanlon
  * Daniel DeMarco 

##### 2. Summarize what problem you want to attack, whether it is EEG-based or Smartphone-based? If you decide to do something different, please justify why your problem serves as an AI project. If you want to use an existing dataset that we have collected or is in a public domain, please state clearly or send us an email to ask for specific datasets. 

We want to do something different than an EEG or smartphone based project.  The problem we wish to address as an AI project dealing with the game of Poker. We found a dataset (https://archive.ics.uci.edu/ml/datasets/Poker+Hand) containing over 1 million unique 5 card poker hands (considering order, suit, and rank). We plan to use it to develop a model using several classification algorithms that can classify what class a hand falls under; where class is the degree of a given poker hand (one pair being the lowest, royal flush the highest). The problem is easy to understand and we want to take advantage of it’s simplicity by applying multiple classification algorithms to it, allowing us to compare the performance of each. It will help us all build a strong foundation of understanding through the use of multiple implementations that accomplish the same goal. This project would also ease the process of dividing work between 7 group members as a result of the independence of each implementation.

##### 3. What kind of datasets you anticipate to collect, or anticipate to use (if using existing datasets)? 

We plan to use a poker dataset collected by http://archive.ics.uci.edu/ml/datasets/Poker+Hand which has already separated the dataset into training and testing sets. The dataset itself has a series of different poker hands classified into different poker hand “ranks”. A poker hand is identified as 5 cards, with 5 different suits and is represented as the first 10 numbers in a 11 size vector. The first 10 numbers corresponds to a suit number (1-4) and a rank order (1-13) of each card in a 5 card poker hand. The last attribute of the vector is the number the poker hand is classified into. 

The classes are: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0: Nothing in hand; not a recognized poker hand <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  1: One pair; one pair of equal ranks within five cards <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  2: Two pairs; two pairs of equal ranks within five cards <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  3: Three of a kind; three equal ranks within five cards <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  4: Straight; five cards, sequentially ranked with no gaps <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  5: Flush; five cards with the same suit <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  6: Full house; pair + different rank three of a kind <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  7: Four of a kind; four equal ranks within five cards <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 8: Straight flush; straight + flush <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 9: Royal flush; {Ace, King, Queen, Jack, Ten} + flush <br>

For example, this vector 1,10,1,11,1,13,1,12,1,1,9 is a poker hand that has a 10 of clubs, 11 (Jack) of clubs, 13 (King) of clubs, 12 (Queen) of clubs, and 1 (Ace) of clubs, and is classified into class 9 which is a royal flush.

##### 4. What AI algorithms you plan to use in your project to address your chosen problem?  How do you plan to evaluate or compare the performance of your chosen algorithms? 

We plan to use several classification algorithms, with the goal of comparing the results to analyze which performs best for the problem as stated. The algorithms we plan to evaluate are gaussian naive bayes, k-nearest neighbor, decisions trees, and Fisher’s discriminant analysis. We plan to use various metrics for performance evaluation for the purpose of model comparison, such as accuracy with confusion matrices, cost matrices, and ROC curves. For model comparison we will consider sensitivity-specificity between models and area under ROC curves.

##### 5. A tentative plan on who is responsible for which part of the project. 

We will assign partners to work on different classification techniques. Among those considered so far, we will most likely work on k-nearest neighbor, gaussian naive bayes, decision trees, and Fisher’s discriminant analysis. If these are implemented quickly, additional techniques may also be considered. For comparison, another pair will work on an ROC curve as a method to compare predicted values run on the test data with their associated true value. If we have additional time, we may also use values from the test set to train the data, and vice-versa, by using random subsampling or bootstrap sampling for instance.
 

