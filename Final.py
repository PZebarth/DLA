import numpy as np
import matplotlib.pyplot as plt
import cv2
# https://pypi.org/project/opencv-python/
# pip install opencv-python // use in command line to install
import glob

def rect_att_plot(length):
                                                                                            
    """
    Parameters
    ----------
    length       : integer
                   length from origin to border of square, or the half length of the full square.   
    """
    
    particles = 10000
    step_number = 30000
    dimension = 2
    step_options = [-1, 0, 1]
    origin = np.zeros((1, dimension))
    boundary = [-length,length]
    stick_coords = np.zeros((1, dimension))
    stick_path = np.zeros((1, dimension))
    
    particle_stick = []
    for i in np.arange(boundary[0],boundary[1]+1):
        
        particle_stick.append([boundary[1],i])
        particle_stick.append([boundary[0],i])
        particle_stick.append([i,boundary[1]])
        particle_stick.append([i,boundary[0]])
    
    particle_stick = np.array(particle_stick)
    particle_stick = np.unique(particle_stick, axis=0)
    
    for j in np.arange(1,particles+1):

        step_shape = [step_number, dimension]
        steps = np.random.choice(a=step_options, size=step_shape)
        path = np.concatenate([origin,steps]).cumsum(0)
    
        for k in np.arange(0,len(path)):
            stuck = False
            for l in np.arange(0,len(particle_stick)):
                if not stuck:
                    if path[k,0] == particle_stick[l,0] and path[k,1] == particle_stick[l,1:]:
                        stick_path = np.concatenate([origin,steps[:k-1]]).cumsum(0)
                        stick_coords = stick_path[-1:]
                        stuck = True
                    else:
                        continue
            if stuck:
                if boundary[0] < stick_coords[:,0] < boundary[1]: 
                    if boundary[0] < stick_coords[:,1] < boundary[1]:
                        particle_stick = np.concatenate([particle_stick,stick_coords])
                        break
        if stick_coords[:,0] == 0 and stick_coords[:,1] == 0:
            break
                    
                    
    plt.scatter(particle_stick[:,0], particle_stick[:,1], alpha=1, color='blue');
    plt.rcParams["figure.figsize"] = (20,20)
    plt.xticks(np.arange(boundary[0],boundary[1]+1,5))
    plt.yticks(np.arange(boundary[0],boundary[1]+1,5))
    plt.show()
    
# rect_att_plot(5)
    
def rect_att_basic_animation(particles, step_number, length, show_path=True,\
                                 with_dots=True, pause=0.0001):
                                                                                           
    """
    Parameters
    ----------
    particles    : integer
                   number of particles
    step_number  : integer
                   number of steps (if no output steps aren't high enough)
    length       : integer
                   length from origin to border of square, or the half length of the full square. 
    show_path    : boolean (optional)
                   If True, random walk path is shown, True by default
    with_dots    : boolean (optional)
                   If True, dots are random-walking particles, True by default. 
    pause        : float (optional)
                   Pausing time between 2 steps, 0.1 secondes by default.   
    """
   
    dimension = 2
    step_options = [-1, 0, 1]
    origin = np.zeros((1, dimension))
    boundary = [-length,length]
    stick_coords = np.zeros((1, dimension))
    stick_path = np.zeros((1, dimension))
    
    particle_stick = []
    for i in np.arange(boundary[0],boundary[1]+1):
        particle_stick.append([boundary[1],i])
        particle_stick.append([boundary[0],i])
        particle_stick.append([i,boundary[1]])
        particle_stick.append([i,boundary[0]])
    
    particle_stick = np.array(particle_stick)
    particle_stick = np.unique(particle_stick, axis=0)
    
    plt.rcParams["figure.figsize"] = (20,20)
    plt.xticks(np.arange(boundary[0],boundary[1]+1,5))
    plt.xlim(boundary[0],boundary[1])
    plt.yticks(np.arange(boundary[0],boundary[1]+1,5))
    plt.ylim(boundary[0],boundary[1])
    
    plt.scatter(particle_stick[:,0], particle_stick[:,1], alpha=1, color='blue')
    
    for j in np.arange(1,particles+1):

        step_shape = [step_number, dimension]
        steps = np.random.choice(a=step_options, size=step_shape)
        path = np.concatenate([origin,steps]).cumsum(0)
    
        for k in np.arange(0,len(path)):
            stuck = False
            for l in np.arange(0,len(particle_stick)):
                if not stuck:
                    if path[k,0] == particle_stick[l,0] and path[k,1] == particle_stick[l,1:]:
                        for m in range(k):
                            stick_path = np.concatenate([origin,steps[:m]]).cumsum(0)
                            if show_path == True and with_dots == False:
                                plt.xticks(np.arange(boundary[0],boundary[1]+1,5))
                                plt.xlim(boundary[0],boundary[1])
                                plt.yticks(np.arange(boundary[0],boundary[1]+1,5))
                                plt.ylim(boundary[0],boundary[1])
                                plt.plot(stick_path[:,0],stick_path[:,1], alpha=0.4, color='red')
                                plt.scatter(particle_stick[:,0], particle_stick[:,1], alpha=0.5,\
                                            color='blue')
                                plt.pause(pause)      
                                plt.show()
                            if with_dots == True and show_path == False:
                                plt.xticks(np.arange(boundary[0],boundary[1]+1,5))
                                plt.xlim(boundary[0],boundary[1])
                                plt.yticks(np.arange(boundary[0],boundary[1]+1,5))
                                plt.ylim(boundary[0],boundary[1])
                                plt.scatter(particle_stick[:,0], particle_stick[:,1], alpha=0.5,\
                                            color='blue')
                                plt.scatter(stick_path[m,0],stick_path[m,1], alpha=0.5, color='blue')
                                plt.pause(pause)
                            if show_path == True and with_dots == True:
                                plt.xticks(np.arange(boundary[0],boundary[1]+1,5))
                                plt.xlim(boundary[0],boundary[1])
                                plt.yticks(np.arange(boundary[0],boundary[1]+1,5))
                                plt.ylim(boundary[0],boundary[1])
                                plt.plot(stick_path[:,0],stick_path[:,1], alpha=0.4, color='red')
                                plt.scatter(particle_stick[:,0], particle_stick[:,1], alpha=0.5,\
                                            color='blue')
                                plt.scatter(stick_path[m,0],stick_path[m,1], alpha=0.5, color='blue')
                                plt.pause(pause)      
                                plt.show()
                            else:
                                plt.scatter(particle_stick[:,0], particle_stick[:,1], alpha=0.5,\
                                            color='blue')
                                
                        stick_coords = stick_path[-1:]
                        stuck = True
    
            if stuck:
                if boundary[0] < stick_coords[:,0] < boundary[1]:
                    if boundary[0] < stick_coords[:,1] < boundary[1]:
                        particle_stick = np.concatenate([particle_stick,stick_coords])
                        break 
                    
        if stick_coords[:,0] == 0 and stick_coords[:,1] == 0:
            break
                 
        if show_path == True:
            plt.xticks(np.arange(boundary[0],boundary[1]+1,5))
            plt.xlim(boundary[0],boundary[1])
            plt.yticks(np.arange(boundary[0],boundary[1]+1,5))
            plt.ylim(boundary[0],boundary[1])
            plt.plot(stick_path[:,0],stick_path[:,1], alpha=0.4, color='red')
            plt.scatter(particle_stick[:,0], particle_stick[:,1], alpha=1, color='blue')
            
        if with_dots == True: 
            plt.xticks(np.arange(boundary[0],boundary[1]+1,5))
            plt.xlim(boundary[0],boundary[1])
            plt.yticks(np.arange(boundary[0],boundary[1]+1,5))
            plt.ylim(boundary[0],boundary[1])
            plt.scatter(particle_stick[:,0], particle_stick[:,1], alpha=1, color='blue')
            plt.show()   
            
# rect_att_basic_animation(1,1000, 5)

def rect_att_animation(length):
                                                                                           
    """
    Instructions
    ----------
    Place this function in a file inside a folder titled Animation on your desktop and set the working 
    directory of the spyder console to the folder Animation on your desktop as well. This function
    read and writes data to that folder. You will have to chane the instance class path_dir to your
    own path directory for this progran to work as intended.
    
    Parameters
    ----------
    length       : integer
                   length from origin to border of square, or the half length of the full square. 
    """

    particles = 10000
    step_number = 30000 
    pause = 0.0001
    dimension = 2
    step_options = [-1, 0, 1]
    origin = np.zeros((1, dimension))
    boundary = [-length,length]
    stick_coords = np.zeros((1, dimension))
    stick_path = np.zeros((1, dimension))
    file_name = "{:09d}_movie.png"
    file_number_adjustment = 1000
    
    particle_stick = []
    for i in np.arange(boundary[0],boundary[1]+1):
        particle_stick.append([boundary[1],i])
        particle_stick.append([boundary[0],i])
        particle_stick.append([i,boundary[1]])
        particle_stick.append([i,boundary[0]])
    
    particle_stick = np.array(particle_stick)
    particle_stick = np.unique(particle_stick, axis=0)
    
    plt.rcParams["figure.figsize"] = (20,20)
    plt.xticks(np.arange(boundary[0],boundary[1]+1,5))
    plt.xlim(boundary[0],boundary[1])
    plt.yticks(np.arange(boundary[0],boundary[1]+1,5))
    plt.ylim(boundary[0],boundary[1])
    plt.scatter(particle_stick[:,0], particle_stick[:,1], alpha=1, color='blue')
    
    count = 0
    
    for j in np.arange(1,particles+1):

        step_shape = [step_number, dimension]
        steps = np.random.choice(a=step_options, size=step_shape)
        path = np.concatenate([origin,steps]).cumsum(0)
        
        for k in np.arange(0,len(path)):
            stuck = False
            for l in np.arange(0,len(particle_stick)):
                if not stuck:
                    if path[k,0] == particle_stick[l,0] and path[k,1] == particle_stick[l,1:]:
                        for m in range(k):
                            stick_path = np.concatenate([origin,steps[:m]]).cumsum(0)
                            plt.xticks(np.arange(boundary[0],boundary[1]+1,5))
                            plt.xlim(boundary[0],boundary[1])
                            plt.yticks(np.arange(boundary[0],boundary[1]+1,5))
                            plt.ylim(boundary[0],boundary[1])
                            plt.scatter(particle_stick[:,0], particle_stick[:,1], alpha=0.5,\
                                        color='blue')
                            plt.scatter(stick_path[m,0],stick_path[m,1], alpha=0.5, color='blue')
                            plt.savefig(file_name.format(m+count))
                            plt.pause(pause)
                        stick_coords = stick_path[-1:]
                        stuck = True

            if stuck:
                if boundary[0] < stick_coords[:,0] < boundary[1]:
                    if boundary[0] < stick_coords[:,1] < boundary[1]:
                        particle_stick = np.concatenate([particle_stick,stick_coords])
                        break 

        if stick_coords[:,0] == 0 and stick_coords[:,1] == 0:
            break

        plt.xticks(np.arange(boundary[0],boundary[1]+1,5))
        plt.xlim(boundary[0],boundary[1])
        plt.yticks(np.arange(boundary[0],boundary[1]+1,5))
        plt.ylim(boundary[0],boundary[1])
        plt.scatter(particle_stick[:,0], particle_stick[:,1], alpha=1, color='blue')
        plt.savefig(file_name.format(k+1+count))
        
        count += file_number_adjustment

    frames = []
    path_dir= '/Users/paulzebarth/Desktop/Animation/*.png'
    
    for filename in sorted(glob.glob(path_dir)):
        frame = cv2.imread(filename)
        height, width, layers = frame.shape
        size = (width,height)
        frames.append(frame)
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('rect_att.mp4', fourcc, fps=30, frameSize = size)
    
    for i in range(len(frames)):
        out.write(frames[i])
    out.release()

# rect_att_animation(5)