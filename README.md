# Knowledge-Graph-Reasoning-with-RL
Knowledge graph is a way of representing information in a structured way using nodes and edges where
nodes represent any subject and edges describe the relation between them. Knowledge graph reasoning
interprets combined semantic information from different sources using a graph base representing
ontologies and derive new information from the existing knowledge. Various applications would be more
promoted if knowledge graph reasoning is applied, e,g., recommendation system, visual question
answering, and structured search.

In recent years, several approaches have been proposed for reasoning graphs including the Path-Ranking
Algorithm (PRA) (Lao et al. 2011), Recurrent Neural Networks + PRA, (Neelakantan et al, 2015). The
Traditional knowledge graph reasoning methods like PRA follow a discrete setup and use random walks
to extract the paths and supervised learning for ranking and Policy gradient methods like REINFORCE
operate in a continuous space.

The motivation of the paper is to reproduce and extend DeepPath (Xiong et. al 2018) which implements
supervised policy learning (which optimizes the problem after converting it to parameterized policy) and
policy gradient methods REINFORCE to reason the graph and identify the improvements of the model
due to the second stage retraining leveraging.

The main issue with DeepPath is that they use REINFORCE, a basic policy gradient method leading to
poor convergence. REINFORCE causes sample inefficiency taking an episode to do the update. However,
there are more advanced state-of-the-art approaches like PPO and Actor critic methods which give much
better results leading to convergence. DeepPath also does not perform a fine-grained analysis of the
experiments carried out.

Thus, We implement Proximal Policy Optimization(PPO), an on-policy method that helps overcome the
challenge of REINFORCE having a high variability, by following a stochastic policy to sample the action
space and also integrate supervised policy learning with PPO. We leverage these three algorithms for
three tasks: (1) link prediction: predict the links between the nodes, (2) node prediction: find the target
entity, given the current node and path, and (3) fact prediction: ranking the true triples among false triples
to indicate whether the facts are true or false. We also performed a fine-grained analysis of the approaches
and presented findings.

Our proposed research questions are (1) Can knowledge graph reasoning be improved by reinforcement
learning compared to other state-of-the-art knowledge graph reasoning algorithms? (2) Does the length
reward function and diverse reward function proposed in DeepPath really help for the KG reasoning
problem?

The main contributions of this paper are five fold: i) We implemented different tasks in knowledge graph
reasoning which gives us a glimpse of the performance of the Reinforcement Learning algorithm in the
knowledge graph reasoning domain. ii) We highlight the significance of using supervised policy learning
along with Policy gradient methods for overcoming the challenge of a bigger action space in the
knowledge graph setting. iii) We evaluate the reward functions for KG reasoning iv) We explored the
SOTA RL algorithm, PPO-Clip on KG reasoning v) We provided fine-grained analysis for the
experiments and and compared each algorithms.
