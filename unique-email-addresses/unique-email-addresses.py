class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local_name, host_name = email.split("@")
            seen.add(local_name.split("+")[0].replace(".", "") + "@" + host_name)
        return len(seen)