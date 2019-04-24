from utils import create_input_files


from macro import IMAGE_FOLDER,OUTPUT_FOLDER

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='flickr30k',  # 'coco',
                       karpathy_json_path='karpathy_split_json_path/dataset_flickr30k.json',  # where data split is divided
                       image_folder=IMAGE_FOLDER,  # '/media/ssd/caption data/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder=OUTPUT_FOLDER,  # ''/media/ssd/caption data/',
                       max_len=50)
