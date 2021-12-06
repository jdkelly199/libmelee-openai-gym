from stable_baselines.common.callbacks import BaseCallback
import csv


class CSVCallback(BaseCallback):
    """
    A custom callback that derives from ``BaseCallback``.

    :param verbose: (int) Verbosity level 0: not output 1: info 2: debug
    """
    def __init__(self, env=None, verbose=0):
        super(CSVCallback, self).__init__(verbose)
        # Those variables will be accessible in the callback
        # (they are defined in the base class)
        # The RL model
        # self.model = None  # type: BaseRLModel
        # An alias for self.model.get_env(), the environment used for training
        # self.training_env = None  # type: Union[gym.Env, VecEnv, None]
        # Number of time the callback was called
        # self.n_calls = 0  # type: int
        # self.num_timesteps = 0  # type: int
        # local and global variables
        # self.locals = None  # type: Dict[str, Any]
        # self.globals = None  # type: Dict[str, Any]
        # The logger object, used to report things in the terminal
        # self.logger = None  # type: logger.Logger
        # # Sometimes, for event callback, it is useful
        # # to have access to the parent object
        # self.parent = None  # type: Optional[BaseCallback]
        self.env = env

        with open('rewards/rewards_callback.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Reward'])  # Give your csv text here.

    def _on_step(self) -> bool:
        """
        This method will be called by the model after each call to `env.step()`.

        For child callback (of an `EventCallback`), this will be called
        when the event is triggered.

        :return: (bool) If the callback returns False, training is aborted early.
        """
        obs = self.env.obs

        with open('rewards/rewards_callback.csv', 'a', newline='') as f:
            writer = csv.writer(f)

            if obs == "New Game":
                writer.writerow([obs])  # Give your csv text here.
            else:
                writer.writerow(obs['observation'])  # Give your csv text here.

        return True
