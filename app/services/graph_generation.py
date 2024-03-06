import pandas as pd
import matplotlib.pyplot as plt
from copy import deepcopy
import base64
from io import BytesIO

class DataFrameVisualizer:
    """
    A class for visualizing DataFrame data using matplotlib and converting plots to base64-encoded images.
    """
    def __init__(self,data_json):

        """
        Initializes the DataFrameVisualizer object with JSON data.

        :param data_json: JSON data representing the DataFrame.
        """
        self.data = pd.read_json(data_json)
        self.row_to_keep = None
    
    def delete (self,what="Total"):
        """
        Deletes a row from the DataFrame based on a specified condition.

        :param what: The value in the first column of the row to be deleted (default is "Total").
        :return: None
        """        
        # Finding the index to delete
        index_delete = self.data.index[self.data[self.data.columns[0]] == what].tolist()[0]
        # Keeping the deleted row for future reference
        self.row_to_keep = self.data.loc[index_delete]
        # Dropping the row from the DataFrame
        self.data = self.data.drop(index_delete)
    
    def save_base64_image(self, plt_obj):

        """
        Saves a matplotlib plot as a base64-encoded image.

        :param plt_obj: Matplotlib plot object to save.
        :return: Base64-encoded image as a string.
        """
        # Create a buffer to store the image data
        buffer = BytesIO()
        # Save the plot to the buffer in PNG format
        plt_obj.savefig(buffer, format='png')
        # Move the buffer's position to the start
        buffer.seek(0)
        # Encode the image data in base64 format
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        # Close the plot object to release resources
        plt_obj.close()
        # Return the base64-encoded image
        return image_base64
    
    def save_base64_to_file(image_base64, file_path):
        """
        Saves a base64-encoded image to a file.

        :param image_base64: Base64-encoded image data as a string.
        :param file_path: Path to save the image file.
        :return: None

        Note: This funtions is for testing the self.save_base64_image()
        """
        # Decode the base64-encoded image data to binary    
        image_data = base64.b64decode(image_base64)
        # Write the binary image data to a file
        with open(file_path, 'wb') as file:
            file.write(image_data)    

    def bar(self):
        """
        Generates a bar plot for all columns in the DataFrame and returns the base64-encoded image.

        :return: Base64-encoded image as a string.
        """
        # Deep copy the DataFrame to avoid modifying the original data
        data = deepcopy(self.data)
        # Extract the data for the x-axis (index)
        eje_x = data.pop(data.columns[0])
        # Iterate over the columns to create separate bars for each column     
        for columna in data.columns:
            plt.bar(eje_x,data[columna], label=columna)
        
        # Adjust x-axis labels for better readability
        plt.xticks(rotation=50,ha='right')
        # Adjust the subplot to prevent overlapping labels
        plt.subplots_adjust(bottom=.4)
        # Add a title to the plot 
        plt.title('Gráfico de todas las columnas del DataFrame')
        # Add a legend to distinguish between columns
        plt.legend()
        # Add grid lines to the plot
        plt.grid()
        # Enable minor ticks on the plot
        plt.minorticks_on()
        # Save the plot as a base64-encoded image
        image_base64 = self.save_base64_image(plt)
        # Return the base64-encoded image
        return image_base64
        
    
    def bar_1v(self,column="Página",column1="Entradas"):
        """
        Generates a bar plot for a single column in the DataFrame and returns the base64-encoded image.

        :param column: The column to plot (default is "Página").
        :param column1: The column representing the bar heights (default is "Entradas").
        :return: Base64-encoded image as a string.
        """
        # Deep copy the DataFrame to avoid modifying the original data
        data = deepcopy(self.data)
        # Extract the data for the x-axis (index)
        eje_x = data.pop(column)
        # Extract the data for the y-axis
        eje_y = data[column1]
        # Create the bar plot
        plt.bar(eje_x,eje_y, label=column1)
        # Adjust x-axis labels for better readability
        plt.xticks(rotation=50,ha='right')
        # Adjust the subplot to prevent overlapping labels
        plt.subplots_adjust(bottom=.4) 
        # Add a title to the plot
        plt.title(column)
        # Add a legend to distinguish between columns
        plt.legend()
        # Add grid lines to the plot
        plt.grid(True)
        # Enable minor ticks on the plot
        plt.minorticks_on()
        # Save the plot as a base64-encoded image
        image_base64 = self.save_base64_image(plt)
        # Return the base64-encoded image
        return image_base64

    def bar_h(self):
        """
        Generates a horizontal bar plot for all columns in the DataFrame and returns the base64-encoded image.

        :return: Base64-encoded image as a string.

        """
        # Deep copy the DataFrame to avoid modifying the original data
        data = deepcopy(self.data)
        # Extract the data for the y-axis
        eje_y = data.pop(data.columns[0])
        # Iterate over the columns to create separate bars for each column
        for columna in data.columns:
            plt.barh(eje_y,data[columna], label=columna)

        # Adjust the subplot to prevent overlapping labels        
        plt.subplots_adjust(left=.4) 
        # Add a title to the plot
        plt.title('Gráfico de todas las columnas del DataFrame')
        # Add a legend to distinguish between columns
        plt.legend()
        # Add grid lines to the plot
        plt.grid(True)
        # Enable minor ticks on the plot
        plt.minorticks_on()
        # Save the plot as a base64-encoded image
        image_base64 = self.save_base64_image(plt)
        # Return the base64-encoded image
        return image_base64
    
    

        
    def barh_1v(self, column="Página", column1="Entradas"):
        """
        Generates a horizontal bar plot for a single column in the DataFrame and returns the base64-encoded image.

        :param column: The column to plot (default is "Página").
        :param column1: The column representing the bar lengths (default is "Entradas").
        :return: Base64-encoded image as a string.
        """
        # Deep copy the DataFrame to avoid modifying the original data
        data = deepcopy(self.data)

        # Extract the data for the x-axis
        eje_x = data.pop(column)
        
        # Extract the data for the y-axis
        eje_y = data[column1]
        
        # Create the horizontal bar plot
        plt.barh(eje_x, eje_y, label=column1)
        
        # Adjust the subplot to prevent overlapping labels
        plt.subplots_adjust(left=.4) 
        
        # Add a title to the plot
        plt.title(column)
        
        # Add a legend to the plot
        plt.legend()
        
        # Add grid lines to the plot
        plt.grid(True)
        
        # Enable minor ticks on the plot
        plt.minorticks_on()
        
        # Save the plot as a base64-encoded image
        image_base64 = self.save_base64_image(plt)
        
        # Return the base64-encoded image
        return image_base64


    def plot(self):
        """
        Generates a line plot for all columns in the DataFrame and returns the base64-encoded image.

        :return: Base64-encoded image as a string.
        """
        # Deep copy the DataFrame to avoid modifying the original data
        data = deepcopy(self.data)

        # Extract the data for the y-axis
        eje_y = data.pop(data.columns[0])
        
        # Iterate over the columns to create separate lines for each column
        for columna in data.columns:
            plt.plot(eje_y, data[columna], label=columna)
        
        # Adjust x-axis labels for better readability
        plt.xticks(rotation=50, ha='right')
        
        # Adjust the subplot to prevent overlapping labels
        plt.subplots_adjust(bottom=.4) 
        
        # Add a title to the plot
        plt.title('Gráfico de todas las columnas del DataFrame')
        
        # Add a legend to distinguish between columns
        plt.legend()
        
        # Add grid lines to the plot
        plt.grid(True)
        
        # Enable minor ticks on the plot
        plt.minorticks_on()
        
        # Save the plot as a base64-encoded image
        image_base64 = self.save_base64_image(plt)
        
        # Return the base64-encoded image
        return image_base64

    def plot_1v(self, column="Página", column1="Entradas"):
        """
        Generates a line plot for a single column in the DataFrame and returns the base64-encoded image.

        :param column: The column to plot on the x-axis (default is "Página").
        :param column1: The column representing the data values (default is "Entradas").
        :return: Base64-encoded image as a string.
        """
        # Deep copy the DataFrame to avoid modifying the original data
        data = deepcopy(self.data)

        # Extract the data for the x-axis
        eje_x = data.pop(column)
        
        # Extract the data for the y-axis
        eje_y = data[column1]
        
        # Create the line plot
        plt.plot(eje_x, eje_y, label=column1)
        
        # Adjust x-axis labels for better readability
        plt.xticks(rotation=50, ha='right')
        
        # Adjust the subplot to prevent overlapping labels
        plt.subplots_adjust(bottom=.4) 
        
        # Add a title to the plot
        plt.title(column)
        
        # Add a legend to the plot
        plt.legend()
        
        # Add grid lines to the plot
        plt.grid(True)
        
        # Enable minor ticks on the plot
        plt.minorticks_on()
        
        # Save the plot as a base64-encoded image
        image_base64 = self.save_base64_image(plt)
        
        # Return the base64-encoded image
        return image_base64
    


    def scatter(self):
        """
        Generates a scatter plot for all columns in the DataFrame and returns the base64-encoded image.

        :return: Base64-encoded image as a string.
        """
        # Deep copy the DataFrame to avoid modifying the original data
        data = deepcopy(self.data)

        # Extract the data for the x-axis
        eje_x = data.pop(data.columns[0])
        
        # Iterate over the columns to create separate scatter plots for each column
        for columna in data.columns:
            plt.scatter(eje_x, data[columna], label=columna)

        # Adjust x-axis labels for better readability
        plt.xticks(rotation=50, ha='right')
        
        # Adjust the subplot to prevent overlapping labels
        plt.subplots_adjust(bottom=.4) 
        
        # Add a title to the plot
        plt.title('Gráfico de todas las columnas del DataFrame')
        
        # Add a legend to distinguish between columns
        plt.legend()
        
        # Add grid lines to the plot
        plt.grid(True)
        
        # Enable minor ticks on the plot
        plt.minorticks_on()
        
        # Save the plot as a base64-encoded image
        image_base64 = self.save_base64_image(plt)
        
        # Return the base64-encoded image
        return image_base64


    def scatter_1v(self, column="Página", column1="Entradas"):
        """
        Generates a scatter plot for a single column in the DataFrame and returns the base64-encoded image.

        :param column: The column to plot on the x-axis (default is "Página").
        :param column1: The column representing the data values (default is "Entradas").
        :return: Base64-encoded image as a string.
        """
        # Deep copy the DataFrame to avoid modifying the original data
        data = deepcopy(self.data)

        # Extract the data for the x-axis
        eje_x = data.pop(column)
        
        # Extract the data for the y-axis
        eje_y = data[column1]
        
        # Create the scatter plot
        plt.scatter(eje_x, eje_y, label=column1)
        
        # Adjust x-axis labels for better readability
        plt.xticks(rotation=50, ha='right')
        
        # Adjust the subplot to prevent overlapping labels
        plt.subplots_adjust(bottom=.4) 
        
        # Add a title to the plot
        plt.title(column)
        
        # Add a legend to the plot
        plt.legend()
        
        # Add grid lines to the plot
        plt.grid(True)
        
        # Enable minor ticks on the plot
        plt.minorticks_on()
        
        # Save the plot as a base64-encoded image
        image_base64 = self.save_base64_image(plt)
        
        # Return the base64-encoded image
        return image_base64
    




 
if __name__ == "__main__":


    "It's for testing "
    image_base64 = []
    Grafica1=DataFrameVisualizer("Prueva_J")          
    Grafica1.delete()
    
    
    image_base64.append(Grafica1.bar())
    image_base64.append(Grafica1.bar_1v())

    image_base64.append(Grafica1.bar_h())
    image_base64.append(Grafica1.barh_1v())

    image_base64.append(Grafica1.plot())
    image_base64.append(Grafica1.plot_1v())

    image_base64.append(Grafica1.scatter())
    image_base64.append(Grafica1.scatter_1v())    
    
    for i in range(len(image_base64)):
        DataFrameVisualizer.save_base64_to_file(image_base64[i],f"{i}.png")
        
    

    