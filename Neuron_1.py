#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random


# In[19]:


[0]*10


# In[61]:


class Network:
    
    def __init__(self,input_neurons,internal_neurons,output_neurons):
        self.input_neurons = input_neurons
        self.output_neurons = output_neurons
        nl = []
        for i in range(input_neurons):
            nl.append(self.Neuron(self,i,0))
        for i in range(internal_neurons):
            nl.append(self.Neuron(self,i+input_neurons,1))
        for i in range(output_neurons):
            nl.append(self.Neuron(self,i+input_neurons+internal_neurons,2))
    
        self.neuron_list = nl
        
    def get_neuron_at_idx(self,idx):
        return self.neuron_list[idx]
        
    def train(self,input_data,output_data,iterations = 1):
        assert len(input_data[0]) == self.input_neurons
        assert len(output_data[0]) == self.output_neurons
        assert len(input_data) == len(output_data)

        while iterations > 0:


            iterations -= 1
        
        print(iterations)
        
            
        
    class Neuron:
        #type 0 is input, type 1 is inner, type 2 is output
        def __init__(self,o_self,neuron_idx,neuron_type=1,default_connects = 2):
            self.type = neuron_type
            self.idx = neuron_idx
            self.down_idx = [] ##the connections that this cell depends on
            self.down_not = [] ##true means just and, false is not in evaluate()
            self.up_idx = [] ##which idx have this neuron in their down_idx
            self.activation = False
            self.correct_count = 0
            self.parent = o_self
            
            if self.type > 0:
                for i in range(default_connects):
                    self.down_idx.append(random.randint(0,self.idx-1))
                    
        def calculate(self):
            for i in self.down_idx:
                print(self.parent.get_neuron_at_idx(i).idx)
                


# In[68]:


n = Network(3,20,3)


# In[69]:


n.input_neurons


# In[70]:


for a in n.neuron_list:
    print(a.idx,a.down_idx)


# In[71]:


n.train([[True,False,True],[True,False,True],[True,False,True]],[[True,True,True],[False,False,True],[True,False,True]],10)


# In[72]:


n.get_neuron_at_idx(15).calculate()


# In[ ]:




