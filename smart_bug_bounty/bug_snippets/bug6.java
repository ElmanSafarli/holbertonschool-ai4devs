// Exercise: recognize the admin role by its text value.
class Bug6 {
    static boolean isAdmin(String role) {
        if (role == null) {
            return false;
        }
        return role == "admin";
    }

    public static void main(String[] args) {
        String fromInput = new String(new char[] {
            'a', 'd', 'm', 'i', 'n'
        });
        System.out.println(isAdmin(fromInput));
        System.out.println(isAdmin("viewer"));
    }
}
