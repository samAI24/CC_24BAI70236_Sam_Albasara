#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;

    ListNode(int x) {
        val = x;
        next = nullptr;
    }
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {

        vector<int> arr;

        while (head != nullptr) {
            arr.push_back(head->val);
            head = head->next;
        }

        int left = 0;
        int right = arr.size() - 1;

        while (left < right) {

            if (arr[left] != arr[right])
                return false;

            left++;
            right--;
        }

        return true;
    }
};

void printList(ListNode* head) {

    while (head != nullptr) {
        cout << head->val;

        if (head->next != nullptr)
            cout << " -> ";

        head = head->next;
    }

    cout << endl;
}

int main() {

    int n;

    cout << "========== Palindrome Linked List (Brute Force) ==========\n";

    cout << "Enter number of nodes: ";
    cin >> n;

    if (n <= 0) {
        cout << "Invalid input.\n";
        return 0;
    }

    cout << "Enter " << n << " values:\n";

    int x;

    cin >> x;
    ListNode* head = new ListNode(x);
    ListNode* temp = head;

    for (int i = 1; i < n; i++) {
        cin >> x;
        temp->next = new ListNode(x);
        temp = temp->next;
    }

    cout << "\nLinked List:\n";
    printList(head);

    Solution obj;

    if (obj.isPalindrome(head))
        cout << "\nResult: The linked list IS a palindrome.\n";
    else
        cout << "\nResult: The linked list IS NOT a palindrome.\n";

    return 0;
}