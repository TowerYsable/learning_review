from __future__ import print_function 
from __future__ import division

import torch.nn as nn
from torchvision import datasets, models


# Top level data directory. Here we assume the format of the directory conforms 
#   to the ImageFolder structure


# Number of classes in the dataset
num_classes = 2

# Batch size for training (change depending on how much memory you have)
BATCH_SIZE = 128      #批处理尺寸(batch_size)


# Flag for feature extracting. When False, we finetune the whole model, 
#   when True we only update the reshaped layer params
feature_extract = True



def set_parameter_requires_grad(model, feature_extracting):
    if feature_extracting:
        for param in model.parameters():
            param.requires_grad = False


def initialize_model(model_name, num_classes, feature_extract, use_pretrained=True):
        # Initialize these variables which will be set in this if statement. Each of these
        #   variables is model specific.
        model_ft = None
        input_size = 0

    if model_name == "resnet":
        """ Resnet18
        """
        model_ft = models.resnet18(pretrained=use_pretrained)
        set_parameter_requires_grad(model_ft, feature_extract)
        num_ftrs = model_ft.fc.in_features
        model_ft.fc = nn.Linear(num_ftrs, num_classes)
        input_size = 224

    elif model_name == "alexnet":
        """ Alexnet
        """
        model_ft = models.alexnet(pretrained=use_pretrained)
        set_parameter_requires_grad(model_ft, feature_extract)
        num_ftrs = model_ft.classifier[6].in_features
        model_ft.classifier[6] = nn.Linear(num_ftrs,num_classes)
        input_size = 224

    elif model_name == "vgg":
        """ VGG11_bn
        """
        model_ft = models.vgg11_bn(pretrained=use_pretrained)
        set_parameter_requires_grad(model_ft, feature_extract)
        num_ftrs = model_ft.classifier[6].in_features
        model_ft.classifier[6] = nn.Linear(num_ftrs,num_classes)
        input_size = 224

    elif model_name == "squeezenet":
        """ Squeezenet
        """
        model_ft = models.squeezenet1_0(pretrained=use_pretrained)
        set_parameter_requires_grad(model_ft, feature_extract)
        model_ft.classifier[1] = nn.Conv2d(512, num_classes, kernel_size=(1,1), stride=(1,1))
        model_ft.num_classes = num_classes
        input_size = 224

    elif model_name == "densenet":
        """ Densenet
        """
        model_ft = models.densenet121(pretrained=use_pretrained)
        set_parameter_requires_grad(model_ft, feature_extract)
        num_ftrs = model_ft.classifier.in_features
        model_ft.classifier = nn.Linear(num_ftrs, num_classes) 
        input_size = 224

    elif model_name == "inception":
        """ Inception v3 
        Be careful, expects (299,299) sized images and has auxiliary output
        """
        model_ft = models.inception_v3(pretrained=use_pretrained)
        set_parameter_requires_grad(model_ft, feature_extract)
        # Handle the auxilary net
        num_ftrs = model_ft.AuxLogits.fc.in_features
        model_ft.AuxLogits.fc = nn.Linear(num_ftrs, num_classes)
        # Handle the primary net
        num_ftrs = model_ft.fc.in_features
        model_ft.fc = nn.Linear(num_ftrs,num_classes)
        input_size = 299

    else:
        print("Invalid model name, exiting...")
        exit()
    
    return model_ft

# Models to choose from [resnet, alexnet, vgg, squeezenet, densenet, inception]
model_name = "vgg"#调用模型的名字
# Initialize the model for this run
model_ft, input_size = initialize_model(model_name, num_classes, feature_extract, use_pretrained=True)

# Print the model we just instantiated
#print(model_ft, input_size)


def extract_feature(model,imgpath):
    model.eval()        # 必须要有，不然会影响特征提取结果
    
    img=Image.open(imgpath)     # 读取图片
    img=img.resize((TARGET_IMG_SIZE, TARGET_IMG_SIZE))
    tensor=img_to_tensor(img)   # 将图片转化成tensor
    tensor=tensor.cuda()    # 如果只是在cpu上跑的话要将这行去掉
    
    result=model(Variable(tensor))
    result_npy=result.data.cpu().numpy()    # 保存的时候一定要记得转成cpu形式的，不然可能会出错
    
    return result_npy[0]    # 返回的矩阵shape是[1, 512, 14, 14]，这么做是为了让shape变回[512, 14,14]
    
if __name__=="__main__":
    model=initialize_model(model_name, num_classes, feature_extract, use_pretrained=True)
    imgpath='/path/to/img.jpg'
    tmp = extract_feature(model, imgpath)
    print(tmp.shape)    # 打印出得到的tensor的shape
    print(tmp)      # 打印出tensor的内容，其实可以换成保存tensor的语句，这里的话就留给读者自由发挥了
