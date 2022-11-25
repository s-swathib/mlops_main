import os 
import argparse #give command as input
import yaml #file to define our configurations
import logging #to log our info

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def main(config_path, datasource):
    config = read_params(config_path)
    print(config)


if __name__=='__main__':
    args = argparse.ArgumentParser()
    default_args_path = os.path.join("config","params.yaml")
    args.add_argument("--config", default=default_args_path)
    args.add_argument("--datasource", default=None)

    parsed_args = args.parse_args()
    #print(parsed_args.config, parsed_args.datasource)
    main(config_path=parsed_args.config, datasource = parsed_args.datasource)
    


