// Exercise: recognize the admin role by its text value.
class Bug6Fixed {
    static boolean isAdmin(String role) {
        return "admin".equals(role);
    }

    public static void main(String[] args) {
        String fromInput = new String(new char[] {
            'a', 'd', 'm', 'i', 'n'
        });
        System.out.println(isAdmin(fromInput));
        System.out.println(isAdmin("viewer"));
    }
}
