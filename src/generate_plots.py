import matplotlib.pyplot as plt
import cv2 
import os


def generate_plots():
    plots_directory = "../plots"
    os.makedirs(plots_directory, exist_ok=True)

    image_names = ["img1.png", "img2.png", "unseen_img1.png", "unseen_img2.png"]

    for i, image_name in enumerate(image_names):

        img = cv2.cvtColor(cv2.imread(f"../data/{image_name}"), cv2.COLOR_BGR2RGB)  
        img_frame = cv2.cvtColor(cv2.imread(f"../frames/frame_{image_name}"), cv2.COLOR_BGR2RGB)  # Replace with your second image path
        img_labeled = cv2.cvtColor(cv2.imread(f"../outputs/barnacles_{image_name}"), cv2.COLOR_BGR2RGB)

        # original image plot
        fig, axes = plt.subplots(1, 3, figsize=(12, 6), dpi=400)
        axes[0].imshow(img)
        axes[0].axis('off')
        axes[0].set_title(f"{image_name}", fontweight='semibold')

        # isolated frame in the image plot
        axes[1].imshow(img_frame)
        axes[1].axis('off')
        axes[1].set_title(f"{image_name} - Frame", fontweight='semibold')

        # barnacles drawn onto the frame plot
        axes[2].imshow(img_labeled)
        axes[2].axis('off')
        axes[2].set_title(f"{image_name} - Labeled", fontweight='semibold')

        fig.suptitle(f"Barnacle Detection Pipeline Overview - {image_name}",
                fontsize=18, fontweight='bold', y=1.02)
        
        new_filename = f"{image_name.split('.')[0]}_overview"


        # Save the plot
        plt.tight_layout()
        plt.savefig(os.path.join(plots_directory, f"{new_filename}.svg"), bbox_inches="tight")
        print(f"Generated new plot '{new_filename}.svg'")   
        
    print(f"\n\nPlots written to folder '{plots_directory}'")
