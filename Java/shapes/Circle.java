import java.lang.Math;

public class Circle implements IShapeMetrics{
    
    private double radius;

    public Circle(double radius){
        this.radius = radius;
    }

    //Prints the radius of the circle
    public String toString(){
        return "Circle with radius: " +String.format("%.2f", this.radius);
    }

    public String name(){
        return "circle";
    }

    //Calculates area
    public double area(){
        return PI * (Math.pow(this.radius, 2));
    }

    //Calculates circumference
    public double circumference(){
        return 2 * PI * this.radius;
    }
}