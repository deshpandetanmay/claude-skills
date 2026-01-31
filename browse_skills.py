#!/usr/bin/env python3
"""
Skills Browser - A simple tool to discover and explore skills in the library
"""

import json
import os
from typing import List, Dict, Optional


def load_catalog() -> Dict:
    """Load the skills catalog."""
    catalog_path = os.path.join(os.path.dirname(__file__), 'skills', 'catalog.json')
    with open(catalog_path, 'r') as f:
        return json.load(f)


def list_all_skills(catalog: Dict) -> None:
    """List all available skills."""
    print("\n" + "="*70)
    print(f"📚 Claude Skills Library - {catalog['stats']['total_skills']} Skills Available")
    print("="*70 + "\n")
    
    # Group skills by category
    skills_by_category = {}
    for skill in catalog['skills']:
        category = skill['category']
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    
    # Find category display info
    category_info = {cat['name']: cat for cat in catalog['categories']}
    
    # Display skills by category
    for category_name, skills in sorted(skills_by_category.items()):
        info = category_info.get(category_name, {})
        icon = info.get('icon', '📦')
        display_name = info.get('display_name', category_name.replace('_', ' ').title())
        
        print(f"{icon} {display_name}")
        print("-" * 70)
        
        for skill in skills:
            deps = skill.get('external_dependencies', [])
            deps_str = f" (requires: {', '.join(deps)})" if deps else ""
            print(f"  • {skill['name']:<25} {skill['description']}{deps_str}")
        print()


def search_skills(catalog: Dict, query: str) -> List[Dict]:
    """Search for skills by name, description, or tags."""
    query = query.lower()
    results = []
    
    for skill in catalog['skills']:
        # Search in name, description, and tags
        if (query in skill['name'].lower() or 
            query in skill['description'].lower() or
            any(query in tag.lower() for tag in skill.get('tags', []))):
            results.append(skill)
    
    return results


def show_skill_details(catalog: Dict, skill_id: str) -> None:
    """Show detailed information about a specific skill."""
    skill = next((s for s in catalog['skills'] if s['id'] == skill_id), None)
    
    if not skill:
        print(f"❌ Skill '{skill_id}' not found.")
        return
    
    print("\n" + "="*70)
    print(f"📦 {skill['name']} (v{skill['version']})")
    print("="*70)
    print(f"\n📝 Description: {skill['description']}")
    print(f"📂 Category: {skill['category']}")
    print(f"💻 Language: {skill['language']}")
    print(f"📊 Difficulty: {skill['difficulty']}")
    print(f"🏷️  Tags: {', '.join(skill.get('tags', []))}")
    
    if skill.get('external_dependencies'):
        print(f"📦 Dependencies: {', '.join(skill['external_dependencies'])}")
    
    print(f"\n📁 Path: {skill['path']}")
    print(f"📖 Documentation: {skill['path']}/README.md")
    print(f"⚙️  Implementation: {skill['path']}/implementation.{skill['language'][:2]}")
    print()


def filter_skills(catalog: Dict, **filters) -> List[Dict]:
    """Filter skills by various criteria."""
    results = catalog['skills'].copy()
    
    if 'category' in filters:
        results = [s for s in results if s['category'] == filters['category']]
    
    if 'difficulty' in filters:
        results = [s for s in results if s.get('difficulty') == filters['difficulty']]
    
    if 'language' in filters:
        results = [s for s in results if s.get('language') == filters['language']]
    
    if 'tag' in filters:
        results = [s for s in results if filters['tag'] in s.get('tags', [])]
    
    return results


def main():
    """Main function for interactive browsing."""
    try:
        catalog = load_catalog()
    except FileNotFoundError:
        print("❌ Error: catalog.json not found. Make sure you're running from the repository root.")
        return
    
    print("🔍 Claude Skills Library Browser")
    print("\nCommands:")
    print("  list           - List all skills")
    print("  search <query> - Search for skills")
    print("  show <id>      - Show details for a skill")
    print("  category <cat> - Filter by category")
    print("  stats          - Show library statistics")
    print("  quit           - Exit")
    
    while True:
        try:
            command = input("\n> ").strip().lower()
            
            if command == 'quit' or command == 'exit':
                print("👋 Goodbye!")
                break
            
            elif command == 'list':
                list_all_skills(catalog)
            
            elif command.startswith('search '):
                query = command[7:].strip()
                results = search_skills(catalog, query)
                if results:
                    print(f"\n🔍 Found {len(results)} skill(s):")
                    for skill in results:
                        print(f"  • {skill['id']}: {skill['name']} - {skill['description']}")
                else:
                    print(f"❌ No skills found matching '{query}'")
            
            elif command.startswith('show '):
                skill_id = command[5:].strip()
                show_skill_details(catalog, skill_id)
            
            elif command.startswith('category '):
                category = command[9:].strip()
                results = filter_skills(catalog, category=category)
                if results:
                    print(f"\n📂 Skills in '{category}':")
                    for skill in results:
                        print(f"  • {skill['name']}: {skill['description']}")
                else:
                    print(f"❌ No skills found in category '{category}'")
            
            elif command == 'stats':
                print("\n" + "="*70)
                print("📊 Library Statistics")
                print("="*70)
                for key, value in catalog['stats'].items():
                    print(f"  {key.replace('_', ' ').title()}: {value}")
                print()
            
            elif command == 'help' or command == '?':
                print("\nCommands:")
                print("  list           - List all skills")
                print("  search <query> - Search for skills")
                print("  show <id>      - Show details for a skill")
                print("  category <cat> - Filter by category")
                print("  stats          - Show library statistics")
                print("  quit           - Exit")
            
            elif command:
                print("❌ Unknown command. Type 'help' for available commands.")
        
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except EOFError:
            print("\n👋 Goodbye!")
            break


if __name__ == "__main__":
    main()
