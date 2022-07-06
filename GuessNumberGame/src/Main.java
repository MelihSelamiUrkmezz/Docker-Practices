
import java.util.Random;
import java.util.Scanner;

/*
 * Melih Selami Urkmez
 * 
 */
public class Main {
    public static void main(String[] args) {
        
        Random rand=new Random();
        
        Scanner scanner=new Scanner(System.in);
        
        int randomnumber=rand.nextInt(50);
        int count=0;
        
        while(true){
            
            System.out.print("Enter your guess:");
            int number=scanner.nextInt();
            
            if(number!=randomnumber){
                count+=1;
                if(number > randomnumber){
                    
                    System.out.println("Your guess is bigger than main number!");
                    System.out.println("Count = "+count);
                }
                
                else{
                    
                    System.out.println("Your guess is smaller than main number!"); 
                    System.out.println("Count = "+count);
                }
            }
            else{
                System.out.println("Congratulations! You find the main number!");
                System.out.println("Count = "+count);
                System.exit(0);
            }
              
            
            
            
        }
        
        
        
        
        
        
               
    }
}
