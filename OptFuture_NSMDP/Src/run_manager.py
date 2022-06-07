import os

# redefine "initial_dict" for every environment, algorithm and speed

if __name__ == '__main__':
    num_seeds = 30
    for i in range(num_seeds):
        initial_dict = {'NN_basis_dim': '16', 'Policy_basis_dim': '32', 'actor_lr': 0.0025151323441388726, 'algo_name': 'ProOLS', 'base': 0, 'batch_size': 1000, 'buffer_size': 1000, 'debug': False, 'delta': 5, 'entropy_lambda': 0.47150591457186375, 'env_name': 'NS_Reacher', 'experiment': 'NS', 'extrapolator_basis': 'Fourier', 'folder_suffix': '660_NS_0_-1_NS_Reacher_Fourier_1000_5_150_3_10.0_0.47150591457186375_0.0025151323441388726_0.0010542534035091538_0.99_False_-1_16_1000_1000_100_rmsprop_True_False_False_False_term_0', 'fourier_coupled': True, 'fourier_k': 3, 'fourier_order': -1, 'gamma': 0.99, 'gauss_std': 1.5, 'gpu': 0, 'hyper': 'Reacher0', 'importance_clip': 10.0, 'inc': 19819, 'log_output': 'term', 'max_episodes': 1000, 'max_inner': 150, 'max_steps': 500, 'optim': 'rmsprop', 'oracle': -1, 'raw_basis': False, 'restore': False, 'save_count': 100, 'save_model': False, 'seed': 19, 'speed': 0, 'state_lr': 0.0010542534035091538, 'summary': True, 'swarm': True, 'timestamp': '8|5|22:11:39'}
        initial_dict.pop('timestamp')
        initial_dict.pop('seed')
        initial_dict['swarm'] = False
        initial_dict['hyper'] = 'default'
        initial_dict['folder_suffix'] = 'Speed3'
        final_string = "--seed="+str(i+1) + " "
        dict_length = len(initial_dict.keys())
        for j, key in enumerate(initial_dict.keys()):
            if type(initial_dict[key]) == str:
                final_string += "--" + key + "='" + str(initial_dict[key]) + "' "
            else:
                final_string += "--" + key + "=" + str(initial_dict[key]) + " "
            if j == dict_length - 1:
                final_string = final_string[:-1]
        os.system(("python run_NS.py " + final_string))


