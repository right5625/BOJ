import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        List<String> strings = new ArrayList<>();

        try
        {
            String str;

            while ((str = br.readLine()) != null)
            {
                String[] AB = str.split(" ");
                int A = Integer.parseInt(AB[0]);
                int B = Integer.parseInt(AB[1]);

                System.out.println(A + B);
            }
        }
        catch (IOException e)
        {
            throw new RuntimeException(e);
        }
    }
}