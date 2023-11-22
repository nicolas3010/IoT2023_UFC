import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pickle
import sklearn
from sklearn import svm
import scipy
with open('modelo.pkl', 'rb') as arquivo:
    clf = pickle.load(arquivo)



def plot_data(fig, hit):

    data = []
    for i, ax in enumerate(fig.axes):

        lines = ax.get_lines()
        x_data = lines[0].get_xdata()
        y_data = []
        subplot_data = []
        for j in range(hit):
            line = lines[j]
            x_data = line.get_xdata()
            y_data.append(line.get_ydata())
            subplot_data.append(y_data[j])

        data.append(subplot_data)


    return data



def plot_time_fig(ecg, dt):
    global clf
    segment_size = 300
    prediction_occurred = False

    for i in range(0, len(ecg) - segment_size + 1, segment_size):
        segment = np.array([ecg[i:i + segment_size]])

        if len(segment[0]) == segment_size:
            result = clf.predict(segment[:, :segment_size].reshape(1, -1))

            if result[0] == 1:
                prediction_occurred = True



    fig, ax = plt.subplots(figsize=(10, 5))

    if prediction_occurred:
        ax.plot(np.arange(len(ecg)) * dt, ecg, label='Exame com presença de arritmia')
        ax.set_title('Exame com presença de arritmia', fontsize=14)
    else:
        ax.plot(np.arange(len(ecg)) * dt, ecg, label='Exame Normal')
        ax.set_title('Exame Normal', fontsize=14)

    ax.set_xlabel('Tempo (s)')
    ax.set_ylabel('Voltagem (V)')

    ax.grid(True)




    return fig


def draw_figure(canvas, figure):

    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg