import java.util.StringTokenizer;

class line_split
{
    public static void main(String[] args)
    {
        StringTokenizer itr = new StringTokenizer("ala ma kota");
        while (itr.hasMoreTokens())
        {
            System.out.println(itr.nextToken());
        }
    }
}
