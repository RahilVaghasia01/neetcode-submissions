class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> group = new HashMap<>();
        for(String s : strs) {
            int[] arr = new int[26];
            for(char c : s.toCharArray()) {
                arr[c - 'a']++;
            }
            String key = Arrays.toString(arr);

            group.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(group.values());
    }
}
