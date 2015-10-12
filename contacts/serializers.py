from rest_framework import serializers
from contacts.models import Contractor, Contact, Group

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
# TODO def update()

class GroupSerializer(serializers.ModelSerializer):
    contractors = ContractorSerializer(many=True)

    class Meta:
        model = Group

    def create(self, validated_data):
        contractors_data = validated_data.pop('contractors')
        group = Group.objects.create(**validated_data)

        for contractor in contractors_data:
            contractor, created = Contractor.objects.get_or_create(name=contractor['name'])
            group.contractors.add(contractor)
        return group
