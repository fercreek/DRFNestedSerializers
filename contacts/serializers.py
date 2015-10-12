from rest_framework import serializers
from contacts.models import Contractor, Contact

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact

class ContractorSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Contractor

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        contractor = Contractor.objects.create(**validated_data)

        for contact in contacts_data:
            contact, created = Contact.objects.get_or_create(name=contact['name'])
            contractor.contacts.add(contact)
        return contractor
