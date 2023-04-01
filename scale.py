import argparse

def rescale_obj(obj_path, obj_scaled_path, scale):
    with open(obj_path, 'r') as source:
        with open(obj_scaled_path, 'w') as target:
            for line in source:
                taget_line = line

                if(line.startswith('v ')):
                    coordinates = [float(coordinate) for coordinate in line.split(' ')[1:]]
                    rescaled = [c*scale for c in coordinates]
                    rescaled_as_str = " ".join([str(c) for c in rescaled])
                    taget_line = f'v {rescaled_as_str}\n'

                target.write(taget_line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("scale.py")
    parser.add_argument("source", help="File to be scaled", type=str)
    parser.add_argument("target", help="Filename in which the scaled file will be saved", type=str)
    parser.add_argument("scale", help="An integer will be increased by 1 and printed.", type=float)
    args = parser.parse_args()

    rescale_obj(args.source, args.target, args.scale)