import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Define parameters

dt = 1/10000
T = 1
n_steps = int(T/dt)
sigma = 0.5
fireUp = 1
fireDown = 0.95
treshold =  0.35
def sim_ddm(treshold=0.35,dt=1/10000,T=1,sigma=0.5,fireUp = 1,fireDown = 0.95):
    
    # open figure with subplots
    fig = make_subplots( shared_xaxes=True)
    # add parameters
    n_steps = int(T/dt)
    noise_term = np.random.normal(0, 1, n_steps) # noise term
    # Simulate the model
    for i in range(1, n_steps):
        # Initialize arrays
        x = np.zeros(n_steps)
        x[0] = 0

        xi = x[i-1]
        xi += (fireUp-fireDown)*dt + sigma*noise_term[i]*np.sqrt(dt)
        x[i] = xi
        if xi >= treshold:
            x[i:] = treshold
            break
        elif xi <= -treshold:
            x[i:] = -treshold
            break

        fig.add_trace(go.Scatter(x=np.arange(n_steps)*dt, y=x, mode='lines', opacity=0.5))

# Plot several runs of the model
for i in range(10):
    sim_ddm()

fig.update_layout(title='Stimuli vs. Reward', xaxis_title='Time (s)', yaxis_title='Decision variable x')
fig.update_layout(height=400, width=600, title_text="Model simulation")
# fig.update_xaxes(title_text='Time (s)', row=2, col=1)
# fig.update_yaxes(title_text='Decision variable x', row=1, col=1)
fig.add_hline(y=treshold, line_dash="dash")
fig.add_hline(y=-treshold, line_dash="dash")

