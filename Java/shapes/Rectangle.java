import java.lang.Math;

public class Rectangle implements IShapeMetrics{
    
    private double height;
    private double width;

    public Rectangle(double height, double width){
        this.height = height;
        this.width = width;
    }

    //Prints the height and width of the rectangle
    public String toString(){
        return "Rectangle with height " +String.format("%.2f", this.height)+ " and width " +String.format("%.2f", this.width);
    }

    public String name(){
        return "rectangle";
    }

    //Calculates the area
    public double area(){
        return this.width * this.height;
    }

    //Calculates circumference
    public double circumference(){
        return (2*this.height) + (2*this.width);
    }
}
