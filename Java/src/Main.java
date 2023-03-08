import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int S = Integer.parseInt(br.readLine());

        if (S >= 90)
        {
            System.out.println("A");
        }
        else if (S >= 80)
        {
            System.out.println("B");
        }
        else if (S >= 70)
        {
            System.out.println("C");
        }
        else if (S >= 60)
        {
            System.out.println("D");
        }
        else
        {
            System.out.println("F");
        }
    }
}