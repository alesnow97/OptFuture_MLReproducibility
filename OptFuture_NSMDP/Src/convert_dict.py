# import os
#
# if __name__ == '__main__':
#     initial_dict = {'NN_basis_dim': '32', 'Policy_basis_dim': '32', 'actor_lr': 0.0013967975033711264, 'algo_name': 'ProOLS', 'base': 0, 'batch_size': 1000, 'buffer_size': 1000, 'debug': False, 'delta': 1, 'entropy_lambda': 0.009309067356364342, 'env_name': 'NS_Reco', 'experiment': 'NS', 'extrapolator_basis': 'Fourier', 'folder_suffix': 'Default', 'fourier_coupled': True, 'fourier_k': 5, 'fourier_order': 3, 'gamma': 0.99, 'gauss_std': 1.5, 'gpu': 0, 'hyper': 'default', 'importance_clip': 15.0, 'inc': 35459, 'log_output': 'term', 'max_episodes': 1000, 'max_inner': 30, 'max_steps': 500, 'optim': 'rmsprop', 'oracle': -1, 'raw_basis': True, 'restore': False, 'save_count': 100, 'save_model': False, 'speed': 0, 'state_lr': 0.001, 'summary': True, 'swarm': False}
#     final_string = ""
#     dict_length = len(initial_dict.keys())
#     for i, key in enumerate(initial_dict.keys()):
#         final_string += "--" + key + "=" + str(initial_dict[key]) + " "
#         if i == dict_length - 1:
#             final_string = final_string[:-1]
#     final_string += " --seed=1"
#     os.system("python run_NS.py " + final_string)

import os

if __name__ == '__main__':
    for i in range(3):
        initial_dict = {'NN_basis_dim': '32', 'Policy_basis_dim': '32', 'actor_lr': 0.007226159368567259, 'algo_name': 'OFPG', 'base': 3000, 'batch_size': 1000, 'buffer_size': 1000, 'debug': False, 'delta': 5, 'entropy_lambda': 0.1, 'env_name': 'NS_SimGlucose-v0', 'experiment': 'NS', 'extrapolator_basis': 'Fourier', 'folder_suffix': '454_NS_3_-1_NS_SimGlucose-v0_Fourier_1000_5_100_5.0_0.007226159368567259_0.99_2.01883_True_3_1000_1000_100_rmsprop_True_False_False_False_term_0', 'fourier_coupled': True, 'fourier_k': 7, 'fourier_order': 3, 'gamma': 0.99, 'gauss_std': 2.01883, 'gpu': 0, 'hyper': 'Diabetes3', 'importance_clip': 5.0, 'inc': 1548, 'log_output': 'term', 'max_episodes': 1000, 'max_inner': 100, 'max_steps': 500, 'optim': 'rmsprop', 'oracle': -1, 'raw_basis': True, 'restore': False, 'save_count': 100, 'save_model': False, 'seed': 8, 'speed': 3, 'state_lr': 0.001, 'summary': True, 'swarm': True, 'timestamp': '8|7|3:52:15'}
        initial_dict.pop('timestamp')
        initial_dict.pop('seed')
        initial_dict['swarm'] = False
        initial_dict['hyper'] = 'default'
        initial_dict['folder_suffix'] = 'Speed3'
        final_string = "--seed="+str(i+1)+" "
        dict_length = len(initial_dict.keys())
        for j, key in enumerate(initial_dict.keys()):
            if type(initial_dict[key]) == str:
                final_string += "--" + key + "='" + str(initial_dict[key]) + "' "
            else:
                final_string += "--" + key + "=" + str(initial_dict[key]) + " "
            if j == dict_length - 1:
                final_string = final_string[:-1]
        os.system(("python run_NS.py " + final_string))


