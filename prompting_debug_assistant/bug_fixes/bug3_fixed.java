// Fixed Bug 3: the last valid index is size() - 1.
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Bug3 {
    public static void main(String[] args) {
        List<String> cities = new ArrayList<>(
            Arrays.asList("Baku", "Tbilisi", "Astana")
        );
        int lastIndex = cities.size() - 1;
        String lastCity = cities.get(lastIndex);
        System.out.println("Last city: " + lastCity);
    }
}
