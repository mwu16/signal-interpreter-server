from routes import signal_interpreter_app, json_parser
from argparse import ArgumentParser

def parse_arguments():
    parser=ArgumentParser()
    parser.add_argument('--file_path')
    return parser.parse_args()

def main():
    args=parse_arguments()
    json_parser.open_file(args.file_path)
    json_parser.load_file(json_parser.data)
    signal_interpreter_app.run()
    
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()