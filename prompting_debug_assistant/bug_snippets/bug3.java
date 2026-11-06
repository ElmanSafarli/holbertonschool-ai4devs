// Bug 3: Runtime exception caused by an invalid index.
// Intended: display the last item in a list.
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Bug3 {
    public static void main(String[] args) {
        List<String> cities = new ArrayList<>(
            Arrays.asList("Baku", "Tbilisi", "Astana")
        );
        int lastIndex = cities.size();
        String lastCity = cities.get(lastIndex);
        System.out.println("Last city: " + lastCity);
    }
}
