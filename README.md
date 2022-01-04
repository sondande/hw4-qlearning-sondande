[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6597221&assignment_repo_type=AssignmentRepo)
# hw4-qlearning
HW4: Stochastic Robot Navigation (Q-Learning)

1. A paragraph (5-10 sentences) comparing the results in your line chart from the first experiment. What trends did you observe about the agent’s learning? How did the agent’s performance change as you varied the learning rate 𝛼? Which learning rate did you find led to the best performance? Please make sure to list the five learning rates compared in your experiment.
   1. From the results of our first experiment, we can see that there was an overall consistency in range throughout all learning rates and that the graph was learning overall. We thought that it was interest that the graph was spiking in the graph but came to the conclusion that
      this was showing how we the graph learned through each episode through the various passages but began to stay relatively consistent through their choices later in the iterations. We found that the best learning rate from our data came from when our alpha value was equal to 0.65 which was a surprise due to the results of when alpha was 035. 
      When looking at the graph, the values in the middle of the graph showed to have higher utilities found when the learning rate was 0.5 but plummeted near the end of our episode iterations. As a result, the 0.65 was what we found to be the most consistent. I believe the pattern between when we choose different rates was if the value was big enough so that the information 
      was useful. This reminds me of the saying "too much of a good thing is bad" and seeing that apply to the data of having a large learning rate requires more time to find the best values but has more opportunity to find worse utilities due to the overall accessibility of how far they are learning. This is interesting as we kept the controlled variable being the exploration aspect of 
      the equation. I think the closer the value was to 1, the more inconsistent the values became in terms of finding similar cumulative utilizes compared to when it was closer to 0. When the value was 0, the values were more consistent, but I believe that to be from the case of using the amount of times a current state chose an action as the denominator of the fraction leaving the learning rate 
      vary dependent on the choices made giving it more consistency.
2. A paragraph (5-10 sentences) comparing the results in your line chart from the second experiment. What trends did you observe about the agent’s learning? How did the agent’s performance change as you varied the exploration rate 𝜖? Which exploration rate did you find led to the best performance? Please make sure to list the five exploration rates compared in your experiment.
   1. 
3. Based on your results from both experiments, what advice would you offer someone new to reinforcement learning about how to choose appropriate values for 𝛼 and 𝜖?
   1. 
4. A short paragraph describing your experience during the assignment (what did you enjoy, what was difficult, etc.)
   1. We Found this lab to be difficult but very interesting overall. Through the process of understanding Deep learning and the application, we could see how our program utilized the information to learn about better paths 
      and costs when going down a path. At first, we were using an action list that held the first default values of a currentState that was not in our dictionary at first. We found that because we originally set up our 
      dictionary to take on multiple lists, it resulted in information being edited and changed. As a result, our program was able to learn from the data it was being given. We found a better method to find the best course of 
      action for our program to take alongside maintaining the values in out Q_table and being able to edit them accordingly based on our current state and generating new Q values through our Q-learning update rule section.
5. 25 hours 
6. We affirm that we have adhered to the honor code on this assignment. - Sagana Ondande & Oliver Rippen
